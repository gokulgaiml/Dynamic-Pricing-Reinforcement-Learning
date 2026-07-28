import joblib
import os


class ModelRegistry:

    def __init__(self):

        self.model_path = "reports/models/pricing_agent.pkl"

        os.makedirs(
            os.path.dirname(self.model_path),
            exist_ok=True
        )

    def save(self, model):

        joblib.dump(model, self.model_path)

        print("Model Saved Successfully")

    def load(self):

        model = joblib.load(self.model_path)

        print("Model Loaded Successfully")

        return model