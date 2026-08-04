import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, PROJECT_ROOT)

from src.models.performance_metrics import PerformanceMetrics

rewards = [
    120,
    135,
    150,
    145,
    160,
    170,
    180,
    175,
    190,
    210
]

metrics = PerformanceMetrics()

metrics.calculate(rewards)