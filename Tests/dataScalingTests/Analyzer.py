from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

X = np.array([[10], [25], [50], [100], [200], [500], [1000], [2000], [5000], [10000]])
y = np.array([25.53003692626953, 26.145800828933716, 27.155039072036743, 29.37702465057373, 34.91813254356384, 50.55793213844299,
              73.65666937828064, 117.10564422607422, 263.486097574234, 516.5872988700867])

regresor = LinearRegression()

regresor.fit(X,y)
Y_pred = regresor.predict(X)

plt.scatter(X, y)
plt.plot(X, Y_pred, color='red')
plt.show()