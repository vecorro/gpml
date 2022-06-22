# This is a definition or declaration file for a Feature Service
# A Feature Service is a convenient way to group related features
# See documentation: https://docs.feast.dev/getting-started/concepts/data-model-and-concepts/feature-service

from feast import FeatureService
from features.feature_views import driver_hourly_stats_view

# Define your feature service and the features it will serve
driver_fs = FeatureService(name="driver_ranking_fv_svc",
                           features=[driver_hourly_stats_view],
                           tags={"description": "Used for training an ElasticNet model"})

