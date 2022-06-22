import mlflow.sklearn 
import feast
import pandas as pd


class DriverRankingPredictModel:
    def __init__(self, repo_path:str, m_uri:str, feature_service_name:str) -> None:
        # Load model from mlflow from the local model registry
        self._model = mlflow.sklearn.load_model(m_uri)

        # Set up feature store and feature service
        self._fs = feast.FeatureStore(repo_path=repo_path)
        self._fsvc = self._fs.get_feature_service(feature_service_name)

    def __call__(self, entity_df):
            return self._predict(entity_df)

    def _predict(self, driver_ids):
        # Read features from Feast
        driver_features = self._fs.get_online_features(
            entity_rows=[{"driver_id": driver_id} for driver_id in driver_ids],
            features=self._fsvc
        )
        df = pd.DataFrame.from_dict(driver_features.to_dict())

        # Make prediction
        df["prediction"] = self._model.predict(df[sorted(df)])

        # Choose best driver
        best_driver_id = df["driver_id"].iloc[df["prediction"].argmax()]

        # return best driver
        return best_driver_id


if __name__ == "__main__":
    mlflow.set_tracking_uri("sqlite:///mlruns.db")
    # Change to your location
    #REPO_PATH = "/Users/jsd/git-repos/feast_workshops/module_1/feature_repo"
    REPO_PATH = "/Users/kike/Library/CloudStorage/OneDrive-VMware,Inc/OCTO/2022-H1/Taurus/Feast/feast_workshops-master/module_1/feature_repo"
    FEATURE_SERVICE_NAME = "driver_ranking_fv_svc"
    model_uri = "models:/sklearn_feast_integration/staging"

    # create an instance of the model
    model = DriverRankingPredictModel(REPO_PATH, model_uri, FEATURE_SERVICE_NAME)
    drivers = [1001, 1002, 1003]
    # model is callable, so just invoke the mode to predict
    best_driver = model(drivers)
    print(f" Best predicted driver for completed trips: {best_driver}")