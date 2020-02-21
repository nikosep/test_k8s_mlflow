import pandas as pd
import os
from random import random, randint
from mlflow import log_metric, log_param, log_artifacts
import mlflow
remote_server_uri = "http://172.16.2.20:8000/"
mlflow.set_tracking_uri(remote_server_uri)
if __name__ == "__main__":
    print("Running mlflow_tracking.py")
    log_param("param1", randint(0, 100))
    log_metric("foo", random())
    log_metric("foo", random() + 1)
    log_metric("foo", random() + 2)
