import pandas as pd
import os


class TrainingHistory:

    def __init__(self):

        os.makedirs("reports", exist_ok=True)

        self.output_file = "reports/training_history.csv"

    def save(self, rewards):

        df = pd.DataFrame({
            "Episode": range(1, len(rewards) + 1),
            "Reward": rewards
        })

        df.to_csv(self.output_file, index=False)

        print("Training history saved successfully.")
        print(df.head())