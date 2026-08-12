import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from src.data.data_loader import DataLoader
from src.rl.pricing_data_environment import PricingDataEnvironment

loader = DataLoader()

data = loader.load()

print("Dataset Loaded")
print("Shape:", data.shape)

env = PricingDataEnvironment(data)

print("\nAction Space:")
print(env.action_space)

print("\nObservation Space:")
print(env.observation_space)

state, info = env.reset()

print("\nInitial State:")
print(state)

action = 2

next_state, reward, terminated, truncated, info = env.step(action)

print("\nAction:")
print(action)

print("\nNext State:")
print(next_state)

print("\nNew Price:")
print(info["new_price"])

print("\nReward:")
print(reward)