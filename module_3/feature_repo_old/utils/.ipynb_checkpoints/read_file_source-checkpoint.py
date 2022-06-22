import pandas as pd

# Change path to your repo
ZIPCODE_TABLE = "/Users/kike/Library/CloudStorage/OneDrive-VMware,Inc/OCTO/2022-H1/Taurus/Feast/feast_workshops-master/module_3/feature_repo/data/zipcode_table.parquet"
LOANS_TABLE = "/Users/kike/Library/CloudStorage/OneDrive-VMware,Inc/OCTO/2022-H1/Taurus/Feast/feast_workshops-master/module_3/feature_repo/data/loan_table.parquet"
CREDIT_HISTORY_TABLE="/Users/kike/Library/CloudStorage/OneDrive-VMware,Inc/OCTO/2022-H1/Taurus/Feast/feast_workshops-master/module_3/feature_repo/data/credit_history.parquet"

if __name__ == "__main__":
    for file in [ZIPCODE_TABLE, LOANS_TABLE, CREDIT_HISTORY_TABLE]:
        df = pd.read_parquet(file)
        pd.set_option('display.max_columns', 15)
        print(f"File: {file}")
        print(df.head(2))
        print(f"Data Source Parquet Shape={df.shape}")
        print(f"columns={df.columns}")