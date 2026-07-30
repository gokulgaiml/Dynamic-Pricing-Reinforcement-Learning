from collections import Counter


class ActionAnalysis:

    def analyze(self, actions):

        count = Counter(actions)

        print("=" * 50)
        print("Pricing Action Analysis")
        print("=" * 50)

        print(f"Increase Price : {count.get('Increase Price', 0)}")
        print(f"Keep Price     : {count.get('Keep Price', 0)}")
        print(f"Decrease Price : {count.get('Decrease Price', 0)}")