import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

import matplotlib.pyplot as plt

from src.data.data_loader import DataLoader
from src.data.cleaner import DataCleaner

loader = DataLoader()
df = loader.load()

clean_df = DataCleaner(df).clean()

cancel = clean_df["is_canceled"].value_counts()

print(cancel)

cancel.index = ["Not Cancelled", "Cancelled"]

cancel.plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(6,6)
)

plt.ylabel("")
plt.title("Booking Cancellation Percentage")

plt.show()
