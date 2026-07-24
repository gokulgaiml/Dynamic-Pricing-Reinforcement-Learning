import random


class PricingAgent:

    def __init__(self):

        self.actions = [
            "Decrease Price",
            "Keep Price",
            "Increase Price"
        ]

    def choose_action(self):

        return random.randint(0, 2)

    def action_name(self, action):

        return self.actions[action]