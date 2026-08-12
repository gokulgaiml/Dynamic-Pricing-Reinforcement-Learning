import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from src.rl.q_learning_agent import QLearningAgent


# Create Q-Learning agent
agent = QLearningAgent(
    state_size=10,
    action_size=3
)


print("Q-Learning Agent Created")

print("\nState Size:")
print(agent.state_size)

print("\nAction Size:")
print(agent.action_size)

print("\nLearning Rate:")
print(agent.learning_rate)

print("\nDiscount Factor:")
print(agent.discount_factor)

print("\nInitial Epsilon:")
print(agent.epsilon)

print("\nInitial Q-Table:")
print(agent.q_table)


# Test action selection
state = 0

action = agent.choose_action(state)

print("\nCurrent State:")
print(state)

print("\nSelected Action:")
print(action)


# Test Q-value update
next_state = 1
reward = 10
terminated = False

agent.update(
    state,
    action,
    reward,
    next_state,
    terminated
)

print("\nUpdated Q-Table:")
print(agent.q_table)


# Test epsilon decay
agent.decay_epsilon()

print("\nEpsilon After Decay:")
print(agent.epsilon)
