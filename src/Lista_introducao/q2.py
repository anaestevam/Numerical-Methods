import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

def f_linha(x):
    h = 0.0001
    return (f(x+h) - f(x)) / h

a = 5
x = np.linspace(2, 8,10)
y = f(x)

reta_tangente = f(a) + f_linha(a) * (x - a)

x_r = a + 2
x_l = a - 2

y_r = f(a) + f_linha(a) * (x_r - a)
y_l = f(a) + f_linha(a) * (x_l - a)


plt.plot(x, reta_tangente, label='reta tangente')
plt.plot(x, y, label='f(x)')
plt.plot(a, f(a), 'ro', label='f(a)='+ str(a))
plt.plot(x_l, y_l, 'bo', label='ponto1='+ str(x_l))
plt.plot(x_r, y_r, 'bo', label='ponto2='+ str(x_r))

plt.legend()
plt.show()
     
