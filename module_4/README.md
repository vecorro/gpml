# Validating historical features with Great Expectations

In this tutorial, we will use the public dataset of Chicago taxi trips to present data validation capabilities of Feast.
The original dataset is stored in BigQuery and consists of raw data for each taxi trip (one row per trip) since 2013.
We will generate several training datasets (aka historical features in Feast) for different periods and evaluate expectations made on one dataset against another.

Types of features we're ingesting and generating:
- Features that aggregate raw data with daily intervals (eg, trips per day, average fare or speed for a specific day, etc.).
- Features using SQL while pulling data from BigQuery (like total trips time or total miles travelled).
-Features calculated on the fly when requested using Feast's on-demand transformations

Our plan:
- Prepare environment
- Pull data from BigQuery (optional)
- Declare & apply features and feature views in Feast
- Generate reference dataset
- Develop & test profiler function
- Run validation on different dataset using reference dataset & profiler

### Steps:
> Open the ```validating-historical-features.ipynb``` from jupyter lab and
> execute the cells to go over the model development process.