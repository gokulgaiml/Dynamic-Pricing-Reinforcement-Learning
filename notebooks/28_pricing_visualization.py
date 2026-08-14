import sys
import os
import joblib

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.rl.pricing_evaluation import PricingEvaluator
from src.utils.pricing_visualization import PricingVisualizer


MODEL_PATH = "reports/models/q_learning_agent.pkl"


print("Loading trained Q-Learning model...")

agent = joblib.load(MODEL_PATH)

print("Model Loaded Successfully")


q_table = agent.q_table

print("\nQ-Table Shape:")
print(q_table.shape)


evaluator = PricingEvaluator(q_table)

decisions = evaluator.evaluate()


print("\nPricing Decisions")
print("=" * 40)

for item in decisions:

    print(
        f"State {item['state']} | "
        f"Action {item['action']} | "
        f"Decision: {item['decision']}"
    )


visualizer = PricingVisualizer()

visualizer.plot_decisions(decisions)