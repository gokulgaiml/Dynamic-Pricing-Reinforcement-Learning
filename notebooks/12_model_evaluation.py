import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, PROJECT_ROOT)

from src.models.evaluation import ModelEvaluation

sample_rewards = [
    120,
    135,
    142,
    150,
    160,
    138,
    145,
    170,
    165,
    155
]

evaluation = ModelEvaluation()

evaluation.evaluate(sample_rewards)