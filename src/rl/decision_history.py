import os
import pandas as pd
from datetime import datetime


class DecisionHistory:

    def __init__(self, output_path="reports/decision_history.csv"):

        self.output_path = output_path

        os.makedirs(
            os.path.dirname(self.output_path),
            exist_ok=True
        )

    def save(self, decisions):

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        records = []

        for item in decisions:

            records.append({
                "timestamp": timestamp,
                "state": item["state"],
                "action": item["action"],
                "decision": item["decision"]
            })

        new_data = pd.DataFrame(records)

        if os.path.exists(self.output_path):

            old_data = pd.read_csv(self.output_path)

            data = pd.concat(
                [old_data, new_data],
                ignore_index=True
            )

        else:

            data = new_data

        data.to_csv(
            self.output_path,
            index=False
        )

        print("Decision History Saved Successfully")
        print(f"Records: {len(new_data)}")
        print(f"History Path: {self.output_path}")

        return data
    