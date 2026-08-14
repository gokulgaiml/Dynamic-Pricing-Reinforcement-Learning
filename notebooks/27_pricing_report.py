import sys
import os
import joblib


sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)


from src.rl.pricing_evaluation import PricingEvaluator
from src.rl.pricing_report import PricingReport


MODEL_PATH = "reports/models/q_learning_agent.pkl"


print("Loading trained Q-Learning model...")

agent = joblib.load(MODEL_PATH)

print("Model Loaded Successfully")


q_table = agent.q_table


print("\nQ-Table Shape:")
print(q_table.shape)


# Create evaluator
evaluator = PricingEvaluator(q_table)


# Generate pricing decisions
decisions = evaluator.evaluate()


print("\nPricing Decisions")
print("=" * 40)

for item in decisions:

    print(
        f"State {item['state']} | "
        f"Action {item['action']} | "
        f"Decision: {item['decision']}"
    )


# Save report
report = PricingReport()

df = report.save(decisions)


print("\nSaved Report Preview")
print("=" * 40)

print(df)