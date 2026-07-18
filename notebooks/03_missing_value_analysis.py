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

missing = clean_df.isnull().sum()
missing = missing[missing > 0]

print("=" * 60)
print("Missing Values")
print("=" * 60)
print(missing)

if len(missing) == 0:
    print("\nNo missing values found after cleaning.")
else:
    plt.figure(figsize=(10,5))

    missing.sort_values().plot(kind="barh")

    plt.title("Missing Values After Cleaning")
    plt.xlabel("Count")

    plt.tight_layout()
    plt.show()