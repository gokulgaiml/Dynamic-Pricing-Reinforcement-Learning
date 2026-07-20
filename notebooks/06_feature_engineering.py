import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from src.data.data_loader import DataLoader
from src.data.cleaner import DataCleaner
from src.features.feature_engineering import FeatureEngineering

loader = DataLoader()

df = loader.load()

clean_df = DataCleaner(df).clean()

engineer = FeatureEngineering(clean_df)

feature_df = engineer.transform()

print(feature_df[[
    "total_nights",
    "total_guests",
    "price_per_guest"
]].head())