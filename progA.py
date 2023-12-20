1 import pandas as pd
2 import matplotlib.pyplot as plt
3 import sklearn
4
5 import seaborn as sns
6 sns.set_style("whitegrid")
7 sns.set_context("poster")
8
9 from sklearn.datasets import load_boston
10 boston load_boston()
11 bos= pd.DataFrame (boston.data)
12 bos.columns = boston. feature_names
13 bos ['PRICE'] = boston. target
14 print (bos.head())
15
16 X = bos.drop( 'PRICE', axis = 1)
17 Y = bos ["PRICE"]
18
19 X train, X_test, Y_train, Y_test= (sklearn.model_selection.
20
21 print (X_train.shape)
22 print (X_test.shape)
23 print (Y_train.shape)
24 print (Y_test.shape)
25
train_test_split(X, Y, test_size = 0.33, random_state = 5))
26 from sklearn. linear_model import LinearRegression
27
28 Lm = LinearRegression()
29 lm. fit(x_train, Y_train)
30
31 Y_pred = Lm.predict(x_test)
32
33 plt.scatter (Y_test, Y_pred)
34 plt.xlabel("Prices: $Y_is")
35 plt.ylabel("Predicted prices: $\hat{Y}_i$")
36 plt.title("Prices vs Predicted prices: $Y_i$ vs $\hat{Y}_i$")
37
38 mse = sklearn.metrics.mean_squared_error(Y_test, Y_pred)
39 print (mse)
40
