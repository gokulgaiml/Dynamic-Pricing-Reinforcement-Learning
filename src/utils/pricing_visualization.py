import matplotlib.pyplot as plt


class PricingVisualizer:

    def plot_decisions(self, decisions):

        decision_counts = {
            "Decrease Price": 0,
            "Keep Price": 0,
            "Increase Price": 0
        }

        for item in decisions:
            decision = item["decision"]
            decision_counts[decision] += 1

        labels = list(decision_counts.keys())
        values = list(decision_counts.values())

        plt.figure(figsize=(10, 5))

        plt.bar(labels, values)

        plt.title("Pricing Decision Distribution")
        plt.xlabel("Pricing Decision")
        plt.ylabel("Number of States")

        plt.tight_layout()
        plt.show()