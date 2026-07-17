import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from src.data.data_loader import DataLoader
from src.data.cleaner import DataCleaner
from src.utils.eda_utils import EDAUtils

loader = DataLoader()
df = loader.load()

clean_df = DataCleaner(df).clean()

EDAUtils.dataset_info(clean_df)

EDAUtils.missing_values(clean_df)

EDAUtils.statistical_summary(clean_df)