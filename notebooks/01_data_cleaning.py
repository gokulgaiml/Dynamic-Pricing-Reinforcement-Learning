import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)
from src.data.data_loader import DataLoader
from src.data.cleaner import DataCleaner

loader = DataLoader()

df = loader.load()

cleaner = DataCleaner(df)

clean_df = cleaner.clean()

print("\nFinal Dataset Shape")

print(clean_df.shape)

print("\nFirst Five Rows")

print(clean_df.head())