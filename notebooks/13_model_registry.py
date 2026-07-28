import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, PROJECT_ROOT)

from src.models.pricing_agent import PricingAgent
from src.models.model_registry import ModelRegistry

agent = PricingAgent()

registry = ModelRegistry()

registry.save(agent)

loaded_model = registry.load()

print(type(loaded_model))