"""
author: atreya
desc:
"""
import datetime
import pandas


class FeatureBuilder():
    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.continuous_features = ["CompetitionDistance","Date"]
        self.categorical_features = ["StoreType", "Assortment"]
        self.target = ["Sales"]

    def featurize(self):
        print "Subsetting Dataframe"
        self.subset_dataframe()
        print "Feature Engineering"
        dataframe =  self.feature_engineering(self.dataframe)
        self.handle_missing_value()
        dataframe = pandas.get_dummies(dataframe)
        print dataframe.head()
        dataframe = self.clean(dataframe)
        return dataframe


    def feature_engineering(self, dataframe=None):
        date1 = [datetime.datetime.strptime(i, '%Y-%m-%d') for i in dataframe.Date]
        dataframe['Day'] = [i.day for i in date1]
        self.continuous_features.append("Day")
        dataframe['Month'] = [i.month for i in date1]
        self.continuous_features.append("Month")
        dataframe['Year'] = [i.year for i in date1]
        self.continuous_features.append("Year")
        dataframe.drop("Date",axis=1,inplace=True)
        return dataframe

    def subset_dataframe(self):
        self.dataframe = self.dataframe[self.continuous_features+self.categorical_features+self.target]

    def handle_missing_value(self):
        self.dataframe.fillna(0, inplace=True)

    def clean(self,df):
        print "Cleaning Unnamed"
        for col in df.columns:
            if 'Unnamed' in col:
                print col
                del df[col]
        return df

