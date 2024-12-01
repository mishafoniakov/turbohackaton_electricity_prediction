from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import mean_squared_error

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Model:
    def __init__(self, model, params):
        self.model = model
        self.params = params

    def grid_search(self, X, y):
        grid = GridSearchCV(self.model, self.params, cv=5)
        grid.fit(X, y)
        best_params = grid.best_params_
        print(best_params)
        return best_params
    
    def feature_importances(self, X, y, n):
        self.model.fit(X, y)
        feature_importances = pd.Series(self.model.feature_importances_, index=X.columns)
        print(list(feature_importances.nlargest(n).index))
        X = X[list(feature_importances.nlargest(n).index)]
        return X
    
    def scores(self, y_test, y_pred):
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        print(f'MSE: {mse}, RMSE: {rmse}')
    
    def plot(self, y_test, y_pred):
        plt.scatter(y_test, y_pred)
        plt.xlabel('Actual')
        plt.ylabel('Predicted')
        plt.show()
