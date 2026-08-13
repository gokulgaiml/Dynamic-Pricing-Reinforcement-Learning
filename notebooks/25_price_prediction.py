import sys
import os


sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from src.rl.price_predictor import PricePredictor


# ---------------------------------------
# Load Trained Agent
# ---------------------------------------

predictor = PricePredictor()


# ---------------------------------------
# Test Different States
# ---------------------------------------

test_states = [0, 1, 2, 3, 4]


print("\nPricing Predictions")
print("=" * 40)


for state in test_states:

    action, action_name = predictor.predict_price_action(
        state
    )

    print(
        f"State: {state} "
        f"| Action: {action} "
        f"| Decision: {action_name}"
    )


# ---------------------------------------
# Display Q-Values
# ---------------------------------------

print("\nQ-Table Decisions")
print("=" * 40)


for state in test_states:

    q_values = predictor.agent.q_table[state]

    print(
        f"State {state} "
        f"| Decrease: {q_values[0]:.2f} "
        f"| Keep: {q_values[1]:.2f} "
        f"| Increase: {q_values[2]:.2f}"
    )