import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, PROJECT_ROOT)

from src.models.pricing_agent import PricingAgent

agent = PricingAgent()

print("=" * 50)
print("Pricing Agent Test")
print("=" * 50)

for i in range(10):

    action = agent.choose_action()

    print(
        "Action",
        i + 1,
        ":",
        agent.action_name(action)
    )