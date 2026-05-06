# app.py — Streamlit frontend for the multi-skill CS 214 tutor demo
import sys
from pathlib import Path

import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parent))
from tutor_engine import SKILLS, run


ASSIGNMENT_WORD_THRESHOLD = 45
SUPPORTED_ASSIGNMENT_FILES = [
    "pdf", "txt", "md", "py", "rkt", "java", "js", "ts",
    "json", "yaml", "yml", "csv", "html", "css",
]


st.set_page_config(
    page_title="CS 214 Multi-Skill Tutor",
    page_icon=":material/school:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={},
)

st.markdown("""
<style>
    #MainMenu, footer, header [data-testid="stToolbar"] {
        visibility: hidden;
        display: none;
    }
    .block-container { max-width: 58rem; padding-top: 1.5rem; }
    [data-testid="stChatMessage"], [data-testid="stMarkdownContainer"], .stMarkdown {
        user-select: text;
        -webkit-user-select: text;
    }
    .skill-card {
        border: 1px solid #e4e7ec;
        border-radius: 0.7rem;
        padding: 0.75rem 0.9rem;
        background: #f8fafc;
        margin-bottom: 0.75rem;
    }
    .skill-label {
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #667085;
        margin-bottom: 0.15rem;
    }
    .skill-name {
        font-size: 1rem;
        font-weight: 650;
        color: #1f2937;
    }
    .small-muted { color: #667085; font-size: 0.85rem; }
</style>
""", unsafe_allow_html=True)


def initialize_state():
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "Hi, I am your CS 214 tutor. Paste your assignment in the "
                    "sidebar or as your first chat message, then ask what you are working on. "
                    "I will route each turn to one skill and guide you with questions."
                ),
            }
        ]
    if "skill_state" not in st.session_state:
        st.session_state.skill_state = {}
    if "assignment" not in st.session_state:
        st.session_state.assignment = ""
    if "assignment_source" not in st.session_state:
        st.session_state.assignment_source = None


def extract_uploaded_assignment(uploaded_file):
    suffix = Path(uploaded_file.name).suffix.lower()
    data = uploaded_file.getvalue()

    if suffix == ".pdf":
        from pypdf import PdfReader

        reader = PdfReader(uploaded_file)
        pages = [page.extract_text() or "" for page in reader.pages]
        return "\n\n".join(page.strip() for page in pages if page.strip())

    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return data.decode("latin-1", errors="replace")


def render_skill_status():
    active_name = st.session_state.skill_state.get("active_skill_name", "None yet")
    display_name = active_name or "None yet"
    status_text = (
        "No active skill"
        if display_name == "None yet"
        else "Guiding the current thread"
    )

    st.markdown(
        f"""
        <div class="skill-card">
            <div class="skill-label">Active Skill</div>
            <div class="skill-name">{display_name}</div>
            <div class="small-muted">{status_text}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


initialize_state()

with st.sidebar:
    st.header("Demo Controls")
    st.caption("Upload or paste your assignment before asking for help.")

    uploaded_assignment = st.file_uploader(
        "Upload assignment file",
        type=SUPPORTED_ASSIGNMENT_FILES,
        help="Drag and drop or browse for a PDF, text file, code file, or markdown prompt.",
    )

    if uploaded_assignment is not None:
        uploaded_key = f"{uploaded_assignment.name}:{uploaded_assignment.size}"
        if st.session_state.assignment_source != uploaded_key:
            try:
                extracted_assignment = extract_uploaded_assignment(uploaded_assignment)
            except Exception as exc:
                st.error(f"Could not read that file: {exc}")
            else:
                if extracted_assignment.strip():
                    st.session_state.assignment = extracted_assignment.strip()
                    st.session_state.assignment_source = uploaded_key
                    st.session_state.skill_state = {}
                    st.success(f"Loaded assignment from {uploaded_assignment.name}.")
                else:
                    st.warning("That file did not contain readable assignment text.")

    st.session_state.assignment = st.text_area(
        "Assignment",
        value=st.session_state.assignment,
        height=260,
        placeholder="Paste the assignment prompt here. No default assignment is loaded.",
    )

    if st.session_state.assignment.strip():
        st.success("Assignment context loaded.")
    else:
        st.warning("No assignment context loaded yet.")

    render_skill_status()

    if st.button("Reset Conversation"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "Conversation reset. Paste your assignment first, then tell me "
                    "what part you are working on."
                ),
            }
        ]
        st.session_state.skill_state = {}
        st.session_state.assignment = ""
        st.session_state.assignment_source = None
        st.rerun()

    st.divider()
    st.caption("Available skills")
    for skill in SKILLS:
        st.markdown(f"- **{skill.name}**")


st.title("CS 214 Multi-Skill Tutor")
st.caption(
    "Exactly one best-matching skill activates per turn. Socratic skills continue "
    "across multiple messages and avoid direct solutions. No default assignment is loaded."
)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


if student_message := st.chat_input(
    "Paste your assignment first, then ask something like: should I print or return?"
):
    st.session_state.messages.append({"role": "user", "content": student_message})
    with st.chat_message("user"):
        st.markdown(student_message)

    if len(student_message.split()) > ASSIGNMENT_WORD_THRESHOLD:
        st.session_state.assignment = student_message

    if not st.session_state.assignment.strip():
        response = (
            "Please paste the assignment prompt first. I need that context before "
            "choosing a skill, otherwise I might route your question based on the wrong assumptions."
        )
        st.session_state.skill_state = {}
        result = {"skill_name": None}
    else:
        result = run({
            "message": student_message,
            "assignment": st.session_state.assignment,
            "history": st.session_state.messages,
            "state": st.session_state.skill_state,
        })

        st.session_state.skill_state = result["state"]
        response = result["response"]

    with st.chat_message("assistant"):
        if result.get("skill_id"):
            caption = f"Skill: {result['skill_name']}"
            if result.get("stance"):
                caption += f" | Stance: {result['stance']}"
            st.caption(caption)
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
