"""
author: atreya
desc:
"""

from sklearn import linear_model
from feature_builder import FeatureBuilder
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import train_test_split

target_variable = ["Sales"]


def train_model_ridge(dataframe):
    print "Training Ridge Regression"
    print dataframe.columns
    ridge = linear_model.Ridge()
    params_grid = {
        "alpha":[0.01,0.05,0.1,0.5]
    }
    X_train, X_test, y_train, y_test = train_test_split(dataframe.drop(target_variable, axis=1),
                                                        dataframe.Sales)
    model = GridSearchCV(ridge, param_grid=params_grid, verbose=2, cv=2, refit=True, n_jobs=1)
    # model = ridge.fit(X_train, y_train)
    model.fit(X_train, y_train)
    return model


def test_model_ridge(dataframe,model):
    df = dataframe.drop(target_variable, axis=1)
    return model.predict(df)

if __name__ == '__main__':
    pass