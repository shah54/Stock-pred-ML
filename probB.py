from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
X, y = make regression (n_samples = 200, n_features=1, noise-8, bias=2)
y2 = y**2
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x, y2)
plt.plot(X, model.predict(X))
import numpy as np
from sklearn.preprocessing import Polynomial Features
poly_features = Polynomial Features (degree = 3)
X_poly poly_features.fit_transform (X)
poly_model.fit (X_poly, y2)
pred poly_model.predict(X_poly)
new_X, new_y = zip(*sorted (zip (X, pred)))
plt.plot(new_X, new_y)
plt.scatter(x, y2)
plt.title("A degree 3 polynoimal")
