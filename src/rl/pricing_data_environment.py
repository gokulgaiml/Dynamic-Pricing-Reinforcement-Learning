import gymnasium as gym
from gymnasium import spaces
import numpy as np
import pandas as pd


class PricingDataEnvironment(gym.Env):

    def __init__(self, data):

        super().__init__()

        self.data = data.reset_index(drop=True)

        self.action_space = spaces.Discrete(3)

        self.observation_space = spaces.Box(
            low=np.array([0.0, 0.0, 0.0], dtype=np.float32),
            high=np.array([1.0, 1000.0, 1000.0], dtype=np.float32),
            dtype=np.float32
        )

        self.current_step = 0

    def _get_state(self):

        row = self.data.iloc[self.current_step]

        demand = 1.0 - float(row["is_canceled"])
        adr = float(row["adr"])
        lead_time = float(row["lead_time"])

        return np.array(
            [demand, adr, lead_time],
            dtype=np.float32
        )

    def reset(self, seed=None, options=None):

        super().reset(seed=seed)

        self.current_step = 0

        state = self._get_state()

        return state, {}

    def step(self, action):

        row = self.data.iloc[self.current_step]

        current_adr = float(row["adr"])

        if action == 0:
            new_price = current_adr * 0.90

        elif action == 1:
            new_price = current_adr

        else:
            new_price = current_adr * 1.10

        demand = 1.0 - float(row["is_canceled"])

        reward = demand * new_price

        self.current_step += 1

        terminated = self.current_step >= len(self.data) - 1
        truncated = False

        if not terminated:
            next_state = self._get_state()
        else:
            next_state = np.zeros(3, dtype=np.float32)

        info = {
            "new_price": new_price,
            "reward": reward
        }

        return next_state, reward, terminated, truncated, info