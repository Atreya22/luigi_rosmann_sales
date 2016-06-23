"""
author: atreya
desc:
"""
import pandas
import os
import pickle
from feature_builder import FeatureBuilder

model_local_path = "/tmp/rossman_sales_model.pkl"

with open(model_local_path,'rb') as f:
    obj = pickle.load(f)

def get_dataframe(json):
    df = pandas.DataFrame.from_dict([dict(json)])
    return df

def predict_sales(json_data=None):
    if json_data is not None:
        df_to_predict = get_dataframe(json_data)
        df_stores_data = pandas.read_csv(os.path.join(os.getcwd(), "data", "store.csv"))
        df_aggregated_to_predict = pandas.merge(df_to_predict, df_stores_data, on='Store')
        fb = FeatureBuilder(df_aggregated_to_predict,training=False)
        dataframe = fb.featurize()
        result = predict(obj["model"],obj["training_features"],dataframe)
        return result[0]
    else:
        return "No Data"


def predict(model_obj=None, trained_features=None, dataframe_predict=None):
    for trained_feature in trained_features:
        if trained_feature not in dataframe_predict.columns:
            dataframe_predict[trained_feature] = 0
    dataframe_predict = dataframe_predict[trained_features]
    y_pred = model_obj.predict(dataframe_predict)
    return y_pred

if __name__ == "__main__":
    data = {
        "Store": 1,
        "DayOfWeek": 4,
        "Date": "2015-09-17",
        "Open": 1,
        "Promo": 1,
        "StateHoliday": 0,
        "SchoolHoliday": 0,
    }
    predict_sales(data)
