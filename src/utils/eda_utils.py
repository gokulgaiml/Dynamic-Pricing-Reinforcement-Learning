import pandas as pd


class EDAUtils:

    @staticmethod
    def dataset_info(df: pd.DataFrame):
        print("=" * 60)
        print("DATASET INFORMATION")
        print("=" * 60)
        print(df.info())

    @staticmethod
    def missing_values(df: pd.DataFrame):
        print("=" * 60)
        print("MISSING VALUES")
        print("=" * 60)
        print(df.isnull().sum())

    @staticmethod
    def statistical_summary(df: pd.DataFrame):
        print("=" * 60)
        print("STATISTICAL SUMMARY")
        print("=" * 60)
        print(df.describe(include="all"))