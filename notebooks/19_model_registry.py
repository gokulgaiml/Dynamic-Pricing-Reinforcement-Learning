import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, PROJECT_ROOT)

from src.models.model_registry import ModelRegistry


dummy_model = {
    "algorithm": "Q-Learning",
    "episodes": 1000,
    "learning_rate": 0.1,
    "discount_factor": 0.95
}

registry = ModelRegistry()

registry.save(dummy_model)

loaded_model = registry.load()

print("\nLoaded Model\n")
print(loaded_model)