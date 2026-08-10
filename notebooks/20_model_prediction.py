import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, PROJECT_ROOT)

from src.models.prediction import PricingPredictor


predictor = PricingPredictor()

states = [
    0.20,
    0.50,
    0.80
]

print("=" * 60)
print("DYNAMIC PRICING MODEL PREDICTION")
print("=" * 60)

for state in states:

    result = predictor.predict(state)

    action = result["action"]

    if action == 0:
        decision = "Decrease Price"
    elif action == 1:
        decision = "Maintain Price"
    else:
        decision = "Increase Price"

    print("\nState:", state)
    print("Action:", action)
    print("Pricing Decision:", decision)

print("\nPrediction completed successfully.")