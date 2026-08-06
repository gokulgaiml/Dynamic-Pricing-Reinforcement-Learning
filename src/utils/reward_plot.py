import matplotlib.pyplot as plt


class RewardPlot:

    def plot_rewards(self, rewards):

        plt.figure(figsize=(10, 5))
        plt.plot(rewards, marker="o")
        plt.title("Training Reward History")
        plt.xlabel("Episode")
        plt.ylabel("Reward")
        plt.grid(True)

        plt.show()

        plt.close()