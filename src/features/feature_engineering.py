import pandas as pd


class FeatureEngineering:

    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def total_nights(self):
        self.df["total_nights"] = (
            self.df["stays_in_weekend_nights"] +
            self.df["stays_in_week_nights"]
        )

    def total_guests(self):
        self.df["total_guests"] = (
            self.df["adults"] +
            self.df["children"] +
            self.df["babies"]
        )

    def booking_per_guest(self):
        self.df["price_per_guest"] = (
            self.df["adr"] /
            self.df["total_guests"].replace(0, 1)
        )

    def transform(self):

        self.total_nights()

        self.total_guests()

        self.booking_per_guest()

        return self.df 