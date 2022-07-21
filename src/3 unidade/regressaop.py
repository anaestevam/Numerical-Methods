import numpy as np, math
import matplotlib.pyplot as plt
x = np.linspace(-2, 2, 100)
y = [2 + 0.5 * xi + 2.1 * xi ** 2 + np.pi * np.random.random() for xi in x]
X = np.transpose(np.array([np.ones(len(x)), x, x**2]))
X1 = np.dot(np.transpose(X),X)
X2 = np.dot(np.linalg.inv(X1), np.transpose(X))
w = np.dot(X2,y)
print('O modelo obtido é f(x) = %.4f + %.4f x + %.4f x*x'%(w[0],w[1],w[2]))
fx = w[0] + w[1]*x + w[2]*x**2
plt.plot(x,y,'o')
plt.plot(x,fx)
plt.show()
