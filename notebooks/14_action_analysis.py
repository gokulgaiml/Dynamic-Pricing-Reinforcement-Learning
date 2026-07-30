import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, PROJECT_ROOT)

from src.utils.action_analysis import ActionAnalysis

actions = [
    "Increase Price",
    "Increase Price",
    "Keep Price",
    "Decrease Price",
    "Increase Price",
    "Keep Price",
    "Decrease Price",
    "Increase Price",
    "Keep Price",
    "Increase Price",
]

analysis = ActionAnalysis()

analysis.analyze(actions)