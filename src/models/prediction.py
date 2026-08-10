import os
import joblib


class PricingPredictor:

    def __init__(self):

        self.model_path = "reports/models/pricing_agent.pkl"

    def load_model(self):

        if not os.path.exists(self.model_path):
            raise FileNotFoundError(
                f"Model not found: {self.model_path}"
            )

        return joblib.load(self.model_path)

    def predict(self, state):

        model = self.load_model()

        # Current model is stored as a dictionary
        # containing the RL configuration.
        if isinstance(model, dict):

            learning_rate = model.get("learning_rate", 0.1)

            if state < 0.33:
                action = 0
            elif state < 0.66:
                action = 1
            else:
                action = 2

            return {
                "action": action,
                "learning_rate": learning_rate
            }

        return model.predict(state)