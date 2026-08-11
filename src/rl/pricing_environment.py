import gymnasium as gym
from gymnasium import spaces
import numpy as np


class PricingEnvironment(gym.Env):

    def __init__(self):

        super().__init__()

        self.action_space = spaces.Discrete(3)

        self.observation_space = spaces.Box(
            low=np.array([0.0, 0.0, 0.0]),
            high=np.array([1.0, 1000.0, 1000.0]),
            dtype=np.float32
        )

        self.state = np.array(
            [0.5, 100.0, 30.0],
            dtype=np.float32
        )

    def reset(self, seed=None, options=None):

        super().reset(seed=seed)

        self.state = np.array(
            [0.5, 100.0, 30.0],
            dtype=np.float32
        )

        return self.state, {}

    def step(self, action):

        demand, adr, lead_time = self.state

        if action == 0:
            adr *= 0.90

        elif action == 1:
            adr *= 1.00

        elif action == 2:
            adr *= 1.10

        revenue = demand * adr

        reward = revenue

        self.state = np.array(
            [demand, adr, max(lead_time - 1, 0)],
            dtype=np.float32
        )

        terminated = lead_time <= 1
        truncated = False

        return self.state, reward, terminated, truncated, {}