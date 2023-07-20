import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 + np.sin(x)

m = 6
x = np.linspace(-np.pi, np.pi, m+1)
y = f(x)
a = np.zeros(m+1)
b = np.zeros(m+1)

for k in range(m+1):
    a[k] = (2/m) * np.sum(y * np.cos(k*x))
    b[k] = (2/m) * np.sum(y * np.sin(k*x))
x_interp = np.linspace(-np.pi, np.pi, 100)
y_interp = np.zeros_like(x_interp)

for i in range(len(x_interp)):
    y_interp[i] = a[0]/2

    for k in range(1, m+1):
        y_interp[i] += a[k] * np.cos(k*x_interp[i]) + b[k] * np.sin(k*x_interp[i])

x_true = np.linspace(-np.pi, np.pi, 100)
y_true = x_true**3 + np.cos(x_true)

plt.plot(x_true, y_true, label='Função x**3+sin(x)')
plt.plot(x, y, 'ro', label='Pontos')
plt.plot(x_interp, y_interp, label='Função interpolada')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolação polinomial trigonométrica')
plt.show()
