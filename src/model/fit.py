import pandas as pd
from sklearn.neighbors import NearestNeighbors
import joblib


def fit_model():
    df_train = pd.read_csv("data/preprocess data/train_data")
    knn = NearestNeighbors(n_neighbors=50, algorithm="auto")
    knn.fit(df_train)
    joblib.dump(knn, "src/model/knn_model.pkl")
    return knn


if __name__ == "__main__":
    fit_model()
