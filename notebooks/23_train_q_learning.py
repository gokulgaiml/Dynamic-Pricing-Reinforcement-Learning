import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from src.data.data_loader import DataLoader
from src.rl.pricing_data_environment import PricingDataEnvironment
from src.rl.q_learning_agent import QLearningAgent


# ---------------------------------------
# 1. Load Dataset
# ---------------------------------------

loader = DataLoader()

data = loader.load()

print("Dataset Shape:")
print(data.shape)


# ---------------------------------------
# 2. Create Pricing Environment
# ---------------------------------------

env = PricingDataEnvironment(data)

print("\nEnvironment Created")
print("Action Space:", env.action_space)
print("Observation Space:", env.observation_space)


# ---------------------------------------
# 3. Create Q-Learning Agent
# ---------------------------------------

agent = QLearningAgent(
    state_size=10,
    action_size=3,
    learning_rate=0.1,
    discount_factor=0.95,
    epsilon=1.0,
    epsilon_decay=0.995,
    epsilon_min=0.01
)

print("\nQ-Learning Agent Created")


# ---------------------------------------
# 4. Training
# ---------------------------------------

episodes = 100

rewards = []

print("\nStarting Training...")


for episode in range(episodes):

    state, info = env.reset()

    # Convert environment state to discrete state
    state_index = episode % agent.state_size

    total_reward = 0

    for step in range(10):

        # Choose pricing action
        action = agent.choose_action(state_index)

        # Take action
        next_state, reward, terminated, truncated, info = env.step(action)

        # Convert next state to discrete index
        next_state_index = (
            (state_index + 1) % agent.state_size
        )

        # Update Q-table
        agent.update(
            state_index,
            action,
            reward,
            next_state_index,
            terminated or truncated
        )

        total_reward += reward

        state_index = next_state_index

        if terminated or truncated:
            break

    # Reduce exploration
    agent.decay_epsilon()

    rewards.append(total_reward)

    if (episode + 1) % 10 == 0:

        print(
            f"Episode {episode + 1}/{episodes} "
            f"| Reward: {total_reward:.2f} "
            f"| Epsilon: {agent.epsilon:.4f}"
        )


# ---------------------------------------
# 5. Training Completed
# ---------------------------------------

print("\nTraining Completed")

print("\nFinal Epsilon:")
print(agent.epsilon)

print("\nFinal Q-Table:")
print(agent.q_table)

print("\nTotal Episodes:")
print(len(rewards))

print("\nTotal Training Reward:")
print(sum(rewards))