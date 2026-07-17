import pandas as pd


class DataCleaner:

    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def remove_duplicates(self):

        before = len(self.df)

        self.df.drop_duplicates(inplace=True)

        after = len(self.df)

        print("=" * 50)
        print("Duplicate Removal")
        print("=" * 50)
        print(f"Rows before : {before}")
        print(f"Rows after  : {after}")
        print(f"Removed     : {before-after}")

    def fill_missing_values(self):

        self.df["children"] = self.df["children"].fillna(0)

        self.df["country"] = self.df["country"].fillna("Unknown")

        self.df["agent"] = self.df["agent"].fillna(0)

        self.df["company"] = self.df["company"].fillna(0)

        print("\nMissing values handled successfully.")

    def clean(self):

        self.remove_duplicates()

        self.fill_missing_values()

        return self.df