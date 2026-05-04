# logic.py — Identify Outputs Skill
import time
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import errors

load_dotenv(Path(__file__).resolve().parent.parent / "example-skill" / ".env")

MODELS = ["gemini-3-flash-preview", "gemini-2.5-flash"]

def load_system_prompt():
  path = Path(__file__).resolve().parent / "skills.md"
  return path.read_text(encoding="utf-8").strip()

def llm_request(contents, max_retries=3):
  client = genai.Client()

  for model in MODELS:
    for attempt in range(max_retries):
      try:
        response = client.models.generate_content(
          model=model, contents=contents
        )
        return response.candidates[0].content.parts[0].text
      except errors.ServerError:
        wait = 2 ** attempt
        print(f"  [{model}] 503 — retrying in {wait}s (attempt {attempt + 1}/{max_retries})")
        time.sleep(wait)

    print(f"  [{model}] all retries exhausted, trying fallback...")

  raise RuntimeError("All models unavailable. Please try again later.")

def run(input):
  """
  input: dict with keys:
      - question: str — the student's question about outputs
      - assignment: str — the full assignment description
      - code: str (optional) — the student's current code
  """
  system_prompt = load_system_prompt()

  user_prompt = f"""
  Student's question:
  {input.get("question")}

  Assignment description:
  {input.get("assignment", "None provided")}

  Student's current code (if any):
  {input.get("code", "None provided")}

  Task:
  Apply the Identify Outputs skill.

  {system_prompt}
  """

  response = llm_request(user_prompt)
  return response
