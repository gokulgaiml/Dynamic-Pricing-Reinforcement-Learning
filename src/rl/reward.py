class RewardFunction:

    def __init__(self):
        pass

    def calculate_reward(self, adr, is_canceled, total_guests):

        reward = adr

        if is_canceled == 1:
            reward -= 50

        reward += total_guests * 5

        return reward