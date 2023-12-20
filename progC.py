import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
mydata = pd. read_csv('HistoricalQuotes.csv')
dataset pd. DataFrame (mydata)
print (dataset)

x = dataset.drop('close', axis = 1)
y = dataset ['close']
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size=0.2, random_state = 123)

from sklearn. linear_model import LinearRegression
Lm LinearRegression()
lm.fit (x_train,y_train)
y_pred lm.predict(x_test)

import matplotlib.pyplot as plt
plt.scatter(y_pred, y_test)
plt.xlabel("Actual Stocks")
plt.ylabel("Predicted Price")
plt.title("Stock of Apple Inc. over the past 3 months")

from sklearn. linear_model import LinearRegression
model = LinearRegression ()
model.fit(x_test, y_test)
plt.plot(y_pred, y_test)
MeanSqEr = sklearn.metrics.mean_squared_error(y_test, y_pred)
print (MeanSqEr)
