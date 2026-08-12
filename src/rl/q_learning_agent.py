import numpy as np


class QLearningAgent:

    def __init__(
        self,
        state_size,
        action_size,
        learning_rate=0.1,
        discount_factor=0.95,
        epsilon=1.0,
        epsilon_decay=0.995,
        epsilon_min=0.01
    ):

        self.state_size = state_size
        self.action_size = action_size

        self.learning_rate = learning_rate
        self.discount_factor = discount_factor

        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min

        self.q_table = np.zeros(
            (state_size, action_size)
        )

    def choose_action(self, state):

        if np.random.random() < self.epsilon:
            return np.random.randint(self.action_size)

        return np.argmax(self.q_table[state])

    def update(
        self,
        state,
        action,
        reward,
        next_state,
        terminated
    ):

        current_q = self.q_table[state, action]

        if terminated:
            target_q = reward
        else:
            target_q = reward + (
                self.discount_factor *
                np.max(self.q_table[next_state])
            )

        self.q_table[state, action] = current_q + (
            self.learning_rate *
            (target_q - current_q)
        )

    def decay_epsilon(self):

        self.epsilon = max(
            self.epsilon_min,
            self.epsilon * self.epsilon_decay
        )