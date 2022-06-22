# This is an example feature declaration file
# You define all your features in a declarative way using Feast declarative APIs
# See documentation: https://rtd.feast.dev/en/latest/#module-feast.feature_view

from google.protobuf.duration_pb2 import Duration
from datasource.file_source import driver_hourly_stats
from feast import Feature, FeatureView, ValueType
from feast import FileSource
from configparser import ConfigParser

# Read data from parquet files. Parquet is convenient for local development mode. For production, you can 
# use your favorite data warehouse (DWH), such as BigQuery or AWS Redshift or S3 modern data lake.
# See Feast documentation for more info.



driver_hourly_stats_view = FeatureView(
    name="driver_hourly_stats",
    entities=["driver_id"],
    ttl=Duration(seconds=86400 * 365),
    features=[
        Feature(name="conv_rate", dtype=ValueType.FLOAT),
        Feature(name="acc_rate", dtype=ValueType.FLOAT),
        Feature(name="avg_daily_trips", dtype=ValueType.INT64),
    ],
    online=True,
    batch_source=driver_hourly_stats,
    tags={},
)
