import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
import joblib


# 70_23.31.10.120
# 0865200000323000217_

class Category:
    df_items = pd.read_csv("data/preprocess data/items_data")
    df_count = pd.read_csv("data/preprocess data/count_data")
    df_pn = pd.read_csv("data/preprocess data/pn_lot")

    def __init__(self):
        self.__mean = 50.08972
        self.__variance = 622.209804
        self.__scaler = StandardScaler()
        self.__model = joblib.load("src/model/knn_model.pkl")

    def get_first_category(self, input_region_code, input_code):
        result = self.df_count[(self.df_count["okpd2_code"] == input_code) &
                               (self.df_count["region_code"] == int(input_region_code))]
        sorted_result = result.sort_values(by="win_count", ascending=False)["supplier"]

        return sorted_result

    def get_second_category(self, input_region_code, input_code):
        self.__scaler.mean_ = self.__mean
        self.__scaler.var_ = self.__variance
        self.__scaler.scale_ = np.sqrt(self.__variance)
        input_embedding = self.df_items[self.df_items["okpd2_code"] == input_code].values[:, 1:]
        input_features = self.__scaler.transform([[input_region_code]])
        input_data = np.concatenate([input_features, input_embedding], axis=1)
        distances, indices = self.__model.kneighbors(input_data)
        ranked_suppliers = self.df_count.iloc[indices[0]]['supplier']

        return ranked_suppliers

    def from_pn_to_str(self, pn_code):
        arr = self.df_pn[self.df_pn["pn_lot"] == pn_code]
        if not arr.empty:
            arr = arr.values[0][1:]
            return str(arr[0]) + "_" + str(arr[1])
        else:
            raise ValueError("Incorrect input")


if __name__ == "__main__":
    print("Please, wait...")
    input_region_code = 66
    input_code = "23.31.10.120"
    cat = Category()
    print(cat.get_first_category(input_region_code, input_code))
    print(cat.get_second_category(input_region_code, input_code))
    print(cat.from_pn_to_str("0865200000323000217_"))

