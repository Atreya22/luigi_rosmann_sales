"""
author: atreya
desc:
"""
import pandas
from luigi_ml_Pipeline import Train
from sklearn.externals import joblib
from feature_builder import FeatureBuilder
from regressor import test_model_ridge


def test():
    df_test = pandas.read_csv("/tmp/test.csv")
    df_stores = pandas.read_csv("/tmp/rossman_sales_train_stores.csv")
    df = pandas.merge(df_test, df_stores, on='Store')
    df["Sales"] = 0
    sales_model = joblib.load(Train().output().path)
    fb = FeatureBuilder(df)
    df = fb.featurize()
    print df.columns
    print test_model_ridge(df,sales_model)


if __name__ == '__main__':
    test()
