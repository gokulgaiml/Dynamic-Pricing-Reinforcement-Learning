import sys
import os
import joblib
import pandas as pd


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
# 2. Create Environment
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


# ---------------------------------------
# 4. Train Agent
# ---------------------------------------

episodes = 100

training_rewards = []


print("\nStarting Training...")


for episode in range(episodes):

    state, info = env.reset()

    state_index = episode % agent.state_size

    total_reward = 0

    for step in range(10):

        action = agent.choose_action(state_index)

        next_state, reward, terminated, truncated, info = env.step(action)

        next_state_index = (
            (state_index + 1) % agent.state_size
        )

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

    agent.decay_epsilon()

    training_rewards.append(total_reward)

    if (episode + 1) % 10 == 0:

        print(
            f"Episode {episode + 1}/{episodes} "
            f"| Reward: {total_reward:.2f} "
            f"| Epsilon: {agent.epsilon:.4f}"
        )


# ---------------------------------------
# 5. Create Model Directory
# ---------------------------------------

os.makedirs(
    "reports/models",
    exist_ok=True
)


# ---------------------------------------
# 6. Save Q-Learning Agent
# ---------------------------------------

model_path = "reports/models/q_learning_agent.pkl"

joblib.dump(
    agent,
    model_path
)

print("\nModel Saved Successfully")
print(model_path)


# ---------------------------------------
# 7. Save Training History
# ---------------------------------------

history = pd.DataFrame(
    {
        "episode": range(1, episodes + 1),
        "reward": training_rewards
    }
)

history_path = "reports/training_rewards.csv"

history.to_csv(
    history_path,
    index=False
)

print("\nTraining History Saved Successfully")
print(history_path)


# ---------------------------------------
# 8. Display Final Results
# ---------------------------------------

print("\nTraining Completed")

print("\nFinal Epsilon:")
print(agent.epsilon)

print("\nTotal Training Reward:")
print(sum(training_rewards))

print("\nAverage Training Reward:")
print(sum(training_rewards) / len(training_rewards))

print("\nFinal Q-Table:")
print(agent.q_table)