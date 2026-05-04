# logic.py — Demo wrapper that delegates to the real identify-outputs skill
import importlib.util
from pathlib import Path

_skill_path = Path(__file__).resolve().parent.parent / "identify-outputs" / "logic.py"
_spec = importlib.util.spec_from_file_location("identify_outputs", _skill_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

run = _mod.run