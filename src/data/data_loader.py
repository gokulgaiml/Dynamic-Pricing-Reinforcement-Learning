import os
import pandas as pd


class DataLoader:

    def __init__(self):

        self.dataset_path = os.path.join(
            os.path.dirname(__file__),
            "hotel_bookings.csv"
        )

    def load(self):

        df = pd.read_csv(self.dataset_path)

        print("Dataset Loaded Successfully")

        print(df.shape)

        return df


if __name__ == "__main__":

    loader = DataLoader()

    df = loader.load()

    print(df.head())