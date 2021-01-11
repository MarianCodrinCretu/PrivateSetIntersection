from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt


with open('scalingReport.txt', 'r') as filex:
    content = filex.read()
    content = content.split('\n\n')[:-1]

    xinitial = []
    yinitial = []

    for x in content:
        print(x)
        splitted = x.split(' ---------- ')
        print(splitted)
        xinitial.append(int(splitted[0]))
        yinitial.append(float(splitted[1]))

X = np.array([[x] for x in xinitial])
y = np.array([y for y in yinitial])

regresor = LinearRegression()

regresor.fit(X,y)
Y_pred = regresor.predict(X)

plt.scatter(X, y)
plt.plot(X, Y_pred, color='red')
plt.savefig('regression.png')