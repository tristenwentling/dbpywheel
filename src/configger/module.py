"""
The entry point of the Python Wheel
"""

def run_config():
    """Sets some global cfg"""
    import os

    try:
        from pyspark.sql import SparkSession
        spark = SparkSession.builder.getOrCreate()
    except ModuleNotFoundError:
        spark = None
        print("Run in a Databricks environment")

    if spark is not None:
        global CURRENT_ENV_FROM_TAG
        CURRENT_ENV_FROM_TAG = spark.conf.get("spark.databricks.clusterUsageTags.CURRENT_ENV")

        global CURRENT_ENV_FROM_VAR
        CURRENT_ENV_FROM_VAR = os.environ.get('KEY_THAT_MIGHT_EXIST')
    else:
        "Unknown Error Encountered"

if __name__ == "__main__":
    try:
        run_config()
    except:
        "Unknown Error Encountered"