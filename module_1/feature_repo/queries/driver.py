import sys
sys.path.insert(0, "../")

from datetime import datetime, timedelta
from pprint import pprint
from pathlib import Path
import pandas as pd

from feast import FeatureStore
from entities.entity import driver
from features.feature_views import driver_hourly_stats_view
from fservice.feature_svc import driver_fs
from train import get_training_data
from fvector import get_feature_vector

# Change this location to yours
# FEAST_REPO = "/Users/jules/git-repos/feast_workshops/module_1/feature_repo/"
FEAST_REPO = "/Users/kike/Library/CloudStorage/OneDrive-VMware,Inc/OCTO/2022-H1/Taurus/Feast/feast_workshops-master/module_1/feature_repo"


if __name__ == "__main__":
    repo_path = Path(FEAST_REPO)
    fs = FeatureStore(repo_path=repo_path)

    # Step 1. Register the data source, entity, features and feature service in the FeatureView with the Feast Registry
    fs.apply([driver, driver_fs, driver_hourly_stats_view])

    # Get the training data
    training_df = get_training_data(repo_path)
    pd.set_option('display.max_columns', 10)
    print(training_df.head())
    print(f"Training data shape: {training_df.shape}")

    # Step 2. Now materialize, load data into online store
    fs.materialize_incremental(end_date=datetime.utcnow())

    # Step 3: Get the feature vector for inference from the online store
    for driver in [1001, 1002, 1003]:
        feature_vector = get_feature_vector(repo_path, driver)
        print("--" * 5)
        pprint(feature_vector)
