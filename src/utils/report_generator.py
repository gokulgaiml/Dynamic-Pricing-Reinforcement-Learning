import os


class ReportGenerator:

    def __init__(self):

        self.report_path = "reports/training_report.txt"

        os.makedirs("reports", exist_ok=True)

    def generate(self, rewards):

        total = sum(rewards)
        average = total / len(rewards)
        maximum = max(rewards)
        minimum = min(rewards)

        with open(self.report_path, "w") as file:

            file.write("Dynamic Pricing using Reinforcement Learning\n")
            file.write("=" * 50 + "\n\n")

            file.write(f"Episodes          : {len(rewards)}\n")
            file.write(f"Total Reward      : {total:.2f}\n")
            file.write(f"Average Reward    : {average:.2f}\n")
            file.write(f"Maximum Reward    : {maximum:.2f}\n")
            file.write(f"Minimum Reward    : {minimum:.2f}\n")

        print("Training report generated successfully.")