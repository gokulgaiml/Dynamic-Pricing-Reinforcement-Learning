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

hotel_counts = clean_df["hotel"].value_counts()

print(hotel_counts)

hotel_counts.plot(
    kind="bar",
    figsize=(6,5)
)

plt.title("Hotel Booking Distribution")
plt.xlabel("Hotel Type")
plt.ylabel("Bookings")

plt.tight_layout()

plt.show()