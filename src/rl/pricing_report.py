import os
import pandas as pd


class PricingReport:

    def __init__(self, output_path="reports/pricing_decisions.csv"):

        self.output_path = output_path

        os.makedirs(
            os.path.dirname(self.output_path),
            exist_ok=True
        )

    def save(self, decisions):

        df = pd.DataFrame(decisions)

        df.to_csv(
            self.output_path,
            index=False
        )

        print("Pricing Report Saved Successfully")
        print(f"Report Path: {self.output_path}")
        print(f"Records Saved: {len(df)}")

        return df