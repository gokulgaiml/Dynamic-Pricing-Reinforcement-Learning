import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from src.rl.pricing_environment import PricingEnvironment


env = PricingEnvironment()

print("Action Space:")
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

print("\nReward:")
print(reward)

print("\nTerminated:")
print(terminated)