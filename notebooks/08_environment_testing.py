import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, PROJECT_ROOT)

from src.data.data_loader import DataLoader
from src.data.cleaner import DataCleaner
from src.features.feature_engineering import FeatureEngineering
from src.features.pricing_features import PricingFeatures
from src.rl.environment import HotelEnvironment

loader = DataLoader()

df = loader.load()

clean_df = DataCleaner(df).clean()

feature_df = FeatureEngineering(clean_df).transform()

pricing_df = PricingFeatures(feature_df).transform()

env = HotelEnvironment(pricing_df)

state = env.reset()

print("Initial State")

print(state.head())

next_state, reward, done = env.step(1)

print()

print("Reward :", reward)

print("Done :", done)