from ast import arg
import os
import argparse
from src.utils.common_utils import (
    read_params,
    create_dir,
    save_local_df, 
    save_reports
)
import pandas as pd 
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error, r2_score
import joblib

def evaluate_metrics(actual, predict):
    rmse = mean_squared_error(actual, predict, squared=False)
    mae = mean_squared_error(actual, predict)
    r2 = r2_score(actual, predict)
    
    return rmse, mae, r2

def evaluate(config_path):
    config = read_params(config_path)
    
    artifacts = config["artifacts"]
    
    split_data = artifacts["split_data"]
    test_data_path = split_data["test_path"]
    
    model_path = artifacts["model_path"]
    
    base = config['base']
    target = base["target_col"]
    scores_file = artifacts["reports"]["scores"]
    
    test = pd.read_csv(test_data_path, sep=",")
    
    test_y = test[target]
    test_x = test.drop(target, axis=1)
    
    lr = joblib.load(model_path)
    
    predict_qualities = lr.predict(test_x) 
    
    rmse, mae, r2 = evaluate_metrics(test_y, predict_qualities)
    
    scores = {
        "rmse": rmse,
        "mae": mae, 
        "r2": r2
    }
    
    save_reports(scores_file, scores)
    
if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parse_args = args.parse_args()
    
    try:
        data = evaluate(config_path=parse_args.config)
    except Exception as e:
        raise e