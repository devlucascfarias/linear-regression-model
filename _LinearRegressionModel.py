import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

class LinearRegressionModel:
    def __init__(self, data_path):
        self.data_path = data_path
        self.model = LinearRegression()

        self.load_data()

        self.train_model()

        print("[3] No errors. Model initialized successfully. \n Code passed.")

    def load_data(self):
        dataframe = pd.read_excel(self.data_path)
        self.X = dataframe.iloc[:, 0].values.reshape(-1, 1)
        self.Y = dataframe.iloc[:, 1].values.reshape(-1, 1)

        print("[1] No errors. Data loaded successfully. \n Code passed." )

    def train_model(self):
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(self.X, self.Y, test_size=0.20)
        self.model.fit(self.X_train, self.Y_train)

        print("[2] No errors. Model trained successfully. \n Code passed.")

    def predict(self, salary):

        salary = np.array(salary).reshape(-1, 1)

        prediction = self.model.predict(salary)

        print("[4] No errors. Prediction made successfully. \n Code passed.")
        
        return prediction

    def evaluate_model(self):
        predictions = self.model.predict(self.X_test)

        print("[5] No errors. Model evaluated successfully. \n Code passed.")
        print('Mean Absolute Error:', metrics.mean_absolute_error(self.Y_test, predictions))


model = LinearRegressionModel('data/BaseDados_RegressaoLinear.xlsx')
print(model.predict(10000))
model.evaluate_model()


