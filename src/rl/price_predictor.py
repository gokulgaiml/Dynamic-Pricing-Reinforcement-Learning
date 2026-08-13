import os
import joblib
import numpy as np


class PricePredictor:

    def __init__(self):

        self.model_path = "reports/models/q_learning_agent.pkl"

        if not os.path.exists(self.model_path):
            raise FileNotFoundError(
                f"Model not found: {self.model_path}"
            )

        self.agent = joblib.load(self.model_path)

        print("Trained Q-Learning Agent Loaded Successfully")

    def predict_action(self, state_index):

        action = np.argmax(
            self.agent.q_table[state_index]
        )

        return int(action)

    def get_action_name(self, action):

        actions = {
            0: "Decrease Price",
            1: "Keep Price",
            2: "Increase Price"
        }

        return actions.get(
            action,
            "Unknown Action"
        )

    def predict_price_action(self, state_index):

        action = self.predict_action(state_index)

        action_name = self.get_action_name(action)

        return action, action_name