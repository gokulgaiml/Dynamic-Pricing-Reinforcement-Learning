import sys
import os
import joblib

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.rl.pricing_evaluation import PricingEvaluator
from src.rl.decision_history import DecisionHistory


MODEL_PATH = "reports/models/q_learning_agent.pkl"


print("Loading trained Q-Learning model...")

agent = joblib.load(MODEL_PATH)

print("Model Loaded Successfully")


q_table = agent.q_table

print("\nQ-Table Shape:")
print(q_table.shape)


evaluator = PricingEvaluator(q_table)

decisions = evaluator.evaluate()


print("\nCurrent Pricing Decisions")
print("=" * 40)

for item in decisions:

    print(
        f"State {item['state']} | "
        f"Action {item['action']} | "
        f"Decision: {item['decision']}"
    )


history = DecisionHistory()

df = history.save(decisions)


print("\nDecision History Preview")
print("=" * 40)

print(df.tail(10))