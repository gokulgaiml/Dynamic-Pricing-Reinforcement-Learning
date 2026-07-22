import random


class HotelEnvironment:

    def __init__(self, dataframe):

        self.df = dataframe

        self.current_step = 0

    def reset(self):

        self.current_step = 0

        return self.df.iloc[self.current_step]

    def step(self, action):

        reward = random.uniform(-5, 10)

        self.current_step += 1

        done = self.current_step >= len(self.df) - 1

        next_state = self.df.iloc[self.current_step]

        return next_state, reward, done

    def state(self):

        return self.df.iloc[self.current_step]