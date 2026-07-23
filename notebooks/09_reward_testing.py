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
from src.rl.reward import RewardFunction

loader = DataLoader()

df = loader.load()

clean_df = DataCleaner(df).clean()

feature_df = FeatureEngineering(clean_df).transform()

pricing_df = PricingFeatures(feature_df).transform()

reward = RewardFunction()

sample = pricing_df.iloc[0]

value = reward.calculate_reward(
    sample["adr"],
    sample["is_canceled"],
    sample["total_guests"]
)

print("=" * 50)
print("Reward Function Test")
print("=" * 50)

print("ADR :", sample["adr"])
print("Guests :", sample["total_guests"])
print("Cancelled :", sample["is_canceled"])
print("Reward :", value)