class PerformanceMetrics:

    def __init__(self):
        pass

    def calculate(self, rewards):

        total_reward = sum(rewards)
        average_reward = total_reward / len(rewards)
        max_reward = max(rewards)
        min_reward = min(rewards)

        improvement = rewards[-1] - rewards[0]

        print("=" * 50)
        print("Reinforcement Learning Performance Metrics")
        print("=" * 50)

        print(f"Episodes           : {len(rewards)}")
        print(f"Total Reward       : {total_reward:.2f}")
        print(f"Average Reward     : {average_reward:.2f}")
        print(f"Maximum Reward     : {max_reward:.2f}")
        print(f"Minimum Reward     : {min_reward:.2f}")
        print(f"Reward Improvement : {improvement:.2f}")