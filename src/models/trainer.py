from src.models.pricing_agent import PricingAgent
from src.rl.reward import RewardFunction


class Trainer:

    def __init__(self):

        self.agent = PricingAgent()
        self.reward_function = RewardFunction()

    def train(self, dataframe):

        total_reward = 0

        for _, row in dataframe.iterrows():

            action = self.agent.choose_action()

            reward = self.reward_function.calculate_reward(
                row["adr"],
                row["is_canceled"],
                row["total_guests"]
            )

            total_reward += reward

        print("=" * 50)
        print("Training Completed")
        print("=" * 50)
        print("Total Reward :", round(total_reward, 2))