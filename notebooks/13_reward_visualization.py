import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, PROJECT_ROOT)

from src.utils.reward_plot import RewardPlot

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

plotter = RewardPlot()

plotter.plot_rewards(rewards)