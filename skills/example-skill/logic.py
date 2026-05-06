"""Compatibility wrapper for the demo tutor engine.

The actual demo app, CLI, and routing logic live in the repo-level utils folder.
This file remains so the example skill's python_entry continues to import cleanly.
"""

import sys
from pathlib import Path

UTILS_DIR = Path(__file__).resolve().parents[2] / "utils"
sys.path.insert(0, str(UTILS_DIR))

from tutor_engine import SKILLS, run