class PricingEvaluator:

    ACTION_NAMES = {
        0: "Decrease Price",
        1: "Keep Price",
        2: "Increase Price"
    }

    def __init__(self, q_table):
        self.q_table = q_table

    def get_best_action(self, state):
        return int(self.q_table[state].argmax())

    def evaluate(self):
        decisions = []

        for state in range(len(self.q_table)):
            action = self.get_best_action(state)

            decisions.append({
                "state": state,
                "action": action,
                "decision": self.ACTION_NAMES[action]
            })

        return decisions

    def print_evaluation(self):

        decisions = self.evaluate()

        print("\nPricing Decision Evaluation")
        print("=" * 40)

        counts = {
            "Decrease Price": 0,
            "Keep Price": 0,
            "Increase Price": 0
        }

        for item in decisions:

            print(
                f"State {item['state']} | "
                f"Action {item['action']} | "
                f"Decision: {item['decision']}"
            )

            counts[item["decision"]] += 1

        total = len(decisions)

        print("\nDecision Distribution")
        print("=" * 40)

        for decision, count in counts.items():

            percentage = (count / total) * 100

            print(
                f"{decision}: "
                f"{count} states "
                f"({percentage:.2f}%)"
            )