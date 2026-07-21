import pandas as pd


class PricingFeatures:

    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def average_price_per_night(self):

        self.df["avg_price_per_night"] = (
            self.df["adr"] /
            self.df["total_nights"].replace(0, 1)
        )

    def weekend_ratio(self):

        self.df["weekend_ratio"] = (
            self.df["stays_in_weekend_nights"] /
            self.df["total_nights"].replace(0, 1)
        )

    def booking_intensity(self):

        self.df["booking_intensity"] = (
            self.df["lead_time"] /
            self.df["total_nights"].replace(0, 1)
        )

    def transform(self):

        self.average_price_per_night()

        self.weekend_ratio()

        self.booking_intensity()

        return self.df