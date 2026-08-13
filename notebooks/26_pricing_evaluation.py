import sys
import os
import joblib

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.rl.pricing_evaluation import PricingEvaluator


MODEL_PATH = "reports/models/q_learning_agent.pkl"


print("Loading trained Q-Learning model...")

agent = joblib.load(MODEL_PATH)

print("Model Loaded Successfully")


# Get Q-table from trained agent object
q_table = agent.q_table

print("\nQ-Table Shape:")
print(q_table.shape)


evaluator = PricingEvaluator(q_table)

evaluator.print_evaluation()