import fire
import mlflow
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_wine

def preprocess_data(data):
    X, y = data.data, data.target
    df = pd.DataFrame(X, columns=data.feature_names)
    df['target'] = y
    return df

def setup_rf_pipeline():
    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    pipe = make_pipeline(StandardScaler(), rf)
    return pipe


def split_data(df, train_size=0.8):
    n_samples = len(df)
    n_train = int(n_samples * train_size)
    df_train = df[:n_train]
    df_test = df[n_train:]
    target = 'target'
    X_train = df_train.drop(target, axis=1)
    X_test = df_test.drop(target, axis=1)
    Y_train = df_train[target]
    Y_test = df_test[target]
    return X_train, X_test, Y_train, Y_test

def track_with_mlflow(model, X_test, Y_test, mlflow):
    mse = ((model.predict(X_test) - Y_test) ** 2).mean()
    rmse = mse ** 0.5
    mlflow.log_metric("rmse", rmse)
    mlflow.log_metric("mse", mse)
    mlflow.sklearn.log_model(model, "model", registered_model_name="sklearn_rf")

def main():
    data = load_wine()
    df = preprocess_data(data)
    X_train, X_test, Y_train, Y_test = split_data(df)
    features = data.feature_names
    with mlflow.start_run():
        rf_pipe = setup_rf_pipeline()
        rf_pipe.fit(X_train, Y_train)
        track_with_mlflow(rf_pipe, X_test, Y_test, mlflow)


if __name__ == "__main__":
    fire.Fire(main)
