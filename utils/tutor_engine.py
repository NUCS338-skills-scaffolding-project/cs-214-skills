"""Multi-skill tutoring demo engine.

This module is intentionally deterministic so the demo can run without an LLM key.
It models the orchestration behavior the real system would provide: route exactly
one skill, keep it active across turns, and respond according to the skill stance.
"""

import importlib.util
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPO_ROOT / "skills"
COMPLETION_PHRASES = (
    "done", "got it", "that helps", "thanks", "thank you",
    "makes sense", "i understand", "i think i have it",
    "i can move on", "move on", "next question",
)


@dataclass(frozen=True)
class SkillSpec:
    skill_id: str
    name: str
    stance: str
    module_dir: Optional[str]
    triggers: tuple[tuple[str, int], ...]
    opening: str
    followups: tuple[str, ...]


SKILLS = [
    SkillSpec(
        skill_id="detect-ambiguity",
        name="Detect Ambiguity",
        stance="socratic",
        module_dir="detect-ambiguity",
        triggers=(
            ("ambiguous", 8), ("unclear", 8), ("vague", 8),
            ("what does this mean", 7), ("not specified", 7),
            ("not sure what they mean", 7), ("reasonable", 5),
            ("properly", 5), ("handle", 3), ("assignment says", 3),
        ),
        opening=(
            "Let's separate the prompt from your assumptions. What exact phrase in "
            "the assignment feels unclear, and what are two possible meanings?"
        ),
        followups=(
            "Which of those interpretations would change your code or tests the most?",
            "What clarification question could you ask that names the two possible behaviors?",
            "Until you get clarification, how will you label your temporary assumption in your notes?",
        ),
    ),
    SkillSpec(
        skill_id="return-behavior",
        name="Decide Return Behavior",
        stance="socratic",
        module_dir="return-behavior",
        triggers=(
            ("print or return", 10), ("return or print", 10),
            ("should i print", 8), ("should i return", 8),
            ("returns none", 8), ("got none", 8), ("side effect", 7),
            ("mutate", 6), ("modify in place", 6), ("helper function", 4),
            ("function contract", 4),
        ),
        opening=(
            "Focus on who needs to observe the result. Is the assignment asking for "
            "a value another function can use, text a person reads, or a changed object?"
        ),
        followups=(
            "What verb does the assignment use: return, print, display, update, or modify?",
            "If you wrote a unit test for this behavior, what would the test be able to observe?",
            "Can you state your current function behavior in one sentence without writing code?",
        ),
    ),
    SkillSpec(
        skill_id="unit-test-plan",
        name="Build a Unit Test Plan",
        stance="socratic",
        module_dir="unit-test-plan",
        triggers=(
            ("test plan", 10), ("testing strategy", 10),
            ("how should i test", 9), ("how do i test", 9),
            ("unit test", 7), ("what tests", 7), ("enough tests", 6),
            ("coverage", 6), ("test matrix", 6),
        ),
        opening=(
            "Let's build a test matrix before writing test code. What are the main "
            "behaviors the assignment requires?"
        ),
        followups=(
            "For each behavior, what is one normal case and one boundary or unusual case?",
            "Which case would catch the bug you are most worried about?",
            "Can you connect each planned test back to a specific requirement from the prompt?",
        ),
    ),
    SkillSpec(
        skill_id="edge-case-tests",
        name="Turn Edge Cases into Tests",
        stance="socratic",
        module_dir="edge-case-tests",
        triggers=(
            ("edge case", 10), ("edge cases", 10), ("corner case", 9),
            ("boundary", 8), ("empty input", 7), ("duplicates", 7),
            ("invalid input", 7), ("what cases", 6), ("missing cases", 6),
        ),
        opening=(
            "Start with the assumptions your code is making. What kind of input would "
            "be smallest, largest, empty, repeated, or otherwise unusual?"
        ),
        followups=(
            "Pick one of those unusual scenarios. What should the expected behavior be?",
            "Which edge case is most likely to break your current logic?",
            "How would you name that case so the test's purpose is clear?",
        ),
    ),
    SkillSpec(
        skill_id="ask-invariant",
        name="Ask for Invariant",
        stance="socratic",
        module_dir="ask-invariant",
        triggers=(
            ("what stays true", 10), ("invariant", 9),
            ("prove my loop", 8), ("why is this correct", 7),
            ("correctness", 6), ("each iteration", 6),
            ("recursive step", 6), ("data structure property", 6),
        ),
        opening=(
            "Before proving the whole thing, name one fact that should stay true "
            "before and after each repeated step. What is that fact in your own words?"
        ),
        followups=(
            "Is that fact true before the first step happens?",
            "Take one ordinary step. What changes, and why should your fact still hold afterward?",
            "How does that fact help explain the final result when the process stops?",
        ),
    ),
    SkillSpec(
        skill_id="identify-inv",
        name="Identify Invariants",
        stance="socratic",
        module_dir="identify-inv",
        triggers=(
            ("loop invariant", 10), ("invariants", 9),
            ("two pointers", 7), ("counter", 5), ("accumulator", 5),
            ("sorted", 4), ("preserve", 6), ("stays true", 8),
            ("data structure invariant", 9),
        ),
        opening=(
            "Let's identify the changing state first. Which variables, indexes, "
            "counters, or structure fields change as your algorithm runs?"
        ),
        followups=(
            "What relationship among those changing pieces should remain true?",
            "Does that relationship hold at the beginning, before the first update?",
            "After one update, what would you check to see whether the relationship was preserved?",
        ),
    ),
    SkillSpec(
        skill_id="trace-state",
        name="Trace State Changes",
        stance="socratic",
        module_dir="trace-state",
        triggers=(
            ("wrong answer", 9), ("wrong result", 9), ("wrong output", 8),
            ("debug", 6), ("trace", 8), ("walk through", 7),
            ("variable", 5), ("infinite loop", 8), ("off by one", 8),
            ("doesn't work", 5),
        ),
        opening=(
            "Let's trace a small case. What is one tiny input where you know the "
            "expected result, and which two or three variables should we track?"
        ),
        followups=(
            "At the start of the first step, what values do those variables hold?",
            "After one iteration or line, which value changes first?",
            "Where does the actual state first differ from what you expected?",
        ),
    ),
    SkillSpec(
        skill_id="error-messages",
        name="Interpret Error Messages",
        stance="socratic",
        module_dir="error-messages",
        triggers=(
            ("traceback", 10), ("syntaxerror", 10), ("indexerror", 10),
            ("keyerror", 10), ("typeerror", 10), ("attributeerror", 10),
            ("recursionerror", 10), ("error message", 8), ("exception", 6),
            ("crash", 6),
        ),
        opening=(
            "Let's use the error as evidence. What is the exact error type and "
            "which line does the traceback point to?"
        ),
        followups=(
            "Right before that line runs, what values and types do the relevant variables have?",
            "What assumption does that line make about the value it is using?",
            "What small input could reproduce the same error with the least extra code?",
        ),
    ),
    SkillSpec(
        skill_id="data-rep-choice",
        name="Choose Data Representation",
        stance="socratic",
        module_dir="data-rep-choice",
        triggers=(
            ("data structure", 8), ("representation", 7),
            ("list or dictionary", 10), ("dict or list", 10),
            ("set or list", 9), ("hash table", 6), ("linked list", 6),
            ("what should i store", 8), ("map", 4), ("lookup", 4),
        ),
        opening=(
            "Start by naming the entities in the problem. What things does your "
            "program need to remember, and how are those things related?"
        ),
        followups=(
            "For the data you named, do order, duplicates, or lookup by key matter?",
            "What operation will happen most often: search, insert, count, update, or iterate?",
            "Which representation seems to fit those operations, and what tradeoff comes with it?",
        ),
    ),
    SkillSpec(
        skill_id="identify-outputs",
        name="Identify Outputs",
        stance="socratic",
        module_dir=None,
        triggers=(
            ("output", 8), ("expected output", 10), ("return", 4),
            ("print", 4), ("format", 6), ("what should it produce", 8),
            ("what am i supposed to output", 10), ("file output", 8),
        ),
        opening=(
            "Look back at the assignment wording. What does it say the code should "
            "produce: a returned value, printed text, stored data, or a file?"
        ),
        followups=(
            "Do the examples show a value being returned or text being displayed?",
            "What type or shape should the final result have?",
            "Can you restate the expected output behavior in one precise sentence?",
        ),
    ),
]


def _normalize(text):
    return re.sub(r"\s+", " ", (text or "").lower()).strip()


def _load_skill_module(skill):
    if not skill.module_dir:
        return None

    path = SKILLS_ROOT / skill.module_dir / "logic.py"
    spec = importlib.util.spec_from_file_location(f"{skill.skill_id}_logic", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _score_skill(skill, message, assignment):
    searchable = message
    score = 0
    matches = []

    for phrase, weight in skill.triggers:
        if phrase in searchable:
            score += weight
            matches.append(phrase)

    return score, matches


def _is_completion_message(message):
    return any(phrase in message for phrase in COMPLETION_PHRASES)


def _choose_skill(message, assignment, state):
    scored = []
    for index, skill in enumerate(SKILLS):
        score, matches = _score_skill(skill, message, assignment)
        scored.append((score, -index, skill, matches))

    scored.sort(reverse=True, key=lambda item: (item[0], item[1]))
    best_score, _, best_skill, best_matches = scored[0]

    active_id = state.get("active_skill_id")
    active_skill = next((skill for skill in SKILLS if skill.skill_id == active_id), None)
    if active_skill and best_score == 0 and not _is_completion_message(message):
        active_score, active_matches = _score_skill(active_skill, message, assignment)
        return active_skill, active_score, active_matches

    if best_score == 0:
        return None, 0, []

    return best_skill, best_score, best_matches


def _skill_input(skill, message, assignment, history):
    common = {
        "message": message,
        "question": message,
        "assignment": assignment,
        "assignment_text": assignment,
        "history": history,
    }

    if skill.skill_id == "error-messages":
        common["error_text"] = message
    elif skill.skill_id in {"ask-invariant", "identify-inv"}:
        common["student_idea"] = message
        common["current_design"] = message
    elif skill.skill_id == "unit-test-plan":
        common["student_code"] = message
    elif skill.skill_id == "return-behavior":
        common["current_design"] = message

    return common


def _call_skill_opening(skill, message, assignment, history):
    module = _load_skill_module(skill)
    if not module:
        return skill.opening

    result = module.run(_skill_input(skill, message, assignment, history))
    if isinstance(result, dict):
        if "prompt" in result:
            return result["prompt"]
        if "guiding_question" in result:
            cause = result.get("likely_cause")
            if cause:
                return f"{cause}\n\n{result['guiding_question']}"
            return result["guiding_question"]
        if "guidance" in result:
            return result["guidance"]

    return str(result)


def _socratic_response(skill, prompt, turn):
    guideline = (
        "I won't give you the final answer, but I'll help you reason it out."
    )
    if turn == 0:
        return f"**{skill.name} activated.** {guideline}\n\n{prompt}"

    return prompt


def _closing_response(skill):
    return (
        f"**{skill.name} complete for now.** You have clarified the key idea enough "
        "to try the next small step yourself. If you hit a new issue, describe what "
        "you are seeing and I will route that message to the most relevant skill."
    )


def _next_prompt(skill, turn):
    if turn <= 0:
        return skill.opening

    followup_index = min(turn - 1, len(skill.followups) - 1)
    return skill.followups[followup_index]


def run(input):
    """
    Route the latest student message to exactly one skill and return a
    multi-turn tutoring response.

    input keys:
        - message: latest student message
        - assignment: assignment text currently in context
        - history: list of chat messages
        - state: dict from the previous run call
    """
    message = input.get("message") or input.get("question") or ""
    assignment = input.get("assignment", "")
    history = input.get("history", [])
    state = dict(input.get("state") or {})

    normalized_message = _normalize(message)
    normalized_assignment = _normalize(assignment)

    if not normalized_message:
        return {
            "skill_id": None,
            "skill_name": "No Skill",
            "stance": None,
            "response": "Tell me what you are working on, and I will help you reason through it.",
            "state": state,
            "matches": [],
        }

    if normalized_assignment == normalized_message and not state.get("assignment_loaded"):
        state["assignment_loaded"] = True
        state["active_skill_id"] = None
        state["active_skill_name"] = None
        state["turn"] = 0
        return {
            "skill_id": None,
            "skill_name": "Assignment Loaded",
            "stance": "meta",
            "response": (
                "Thanks, I have the assignment context now. What part are you working "
                "on first: outputs, data representation, testing, debugging, ambiguity, "
                "or correctness reasoning?"
            ),
            "state": state,
            "matches": ["assignment-context"],
        }

    active_id = state.get("active_skill_id")
    active_skill = next((item for item in SKILLS if item.skill_id == active_id), None)

    if active_skill and _is_completion_message(normalized_message):
        state["active_skill_id"] = None
        state["active_skill_name"] = None
        state["turn"] = 0
        state["assignment_loaded"] = bool(state.get("assignment_loaded") or assignment)
        return {
            "skill_id": active_skill.skill_id,
            "skill_name": active_skill.name,
            "stance": active_skill.stance,
            "response": _closing_response(active_skill),
            "state": state,
            "matches": ["student-completed-skill"],
            "switched": False,
            "completed": True,
        }

    skill, _score, matches = _choose_skill(
        normalized_message,
        normalized_assignment,
        state,
    )

    if skill is None:
        state["assignment_loaded"] = bool(state.get("assignment_loaded") or assignment)
        return {
            "skill_id": None,
            "skill_name": "No Skill Triggered",
            "stance": None,
            "response": (
                "I need a little more detail to choose the right skill. What are you "
                "trying to decide, debug, test, or clarify in the assignment?"
            ),
            "state": state,
            "matches": [],
            "switched": False,
        }

    switched = state.get("active_skill_id") != skill.skill_id
    turn = 0 if switched else state.get("turn", 0) + 1

    if not switched and turn > len(skill.followups):
        state["active_skill_id"] = None
        state["active_skill_name"] = None
        state["turn"] = 0
        state["assignment_loaded"] = bool(state.get("assignment_loaded") or assignment)
        return {
            "skill_id": skill.skill_id,
            "skill_name": skill.name,
            "stance": skill.stance,
            "response": _closing_response(skill),
            "state": state,
            "matches": ["skill-followups-complete"],
            "switched": False,
            "completed": True,
        }

    if turn == 0:
        prompt = _call_skill_opening(skill, message, assignment, history)
    else:
        prompt = _next_prompt(skill, turn)

    response = _socratic_response(skill, prompt, turn)

    state["active_skill_id"] = skill.skill_id
    state["active_skill_name"] = skill.name
    state["turn"] = turn
    state["assignment_loaded"] = bool(state.get("assignment_loaded") or assignment)

    return {
        "skill_id": skill.skill_id,
        "skill_name": skill.name,
        "stance": skill.stance,
        "response": response,
        "state": state,
        "matches": matches,
        "switched": switched,
    }
