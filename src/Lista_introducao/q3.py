import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

def f_linha(x):
    return np.cos(x)

def f_2_linha(x):
    return -np.sin(x)

def taylor(a, x):
    return f(a) + f_linha(a)*(x-a) + f_2_linha(a)*((x-a)**2)/2

x = np.linspace(-5, 10, 1000)
a = 2
x_l = a - 5
x_r = a + 5

poli_taylor = taylor(a, x)
p_l = taylor(a, x_l)
p_r = taylor(a, x_r)

fig, ax = plt.subplots()

ax.plot(x, poli_taylor, label='polinomio de taylor')
ax.plot(x, f(x), label='f(x)')
ax.plot([x_l, a, x_r], [p_l, f(a), p_r], 'bo', label='pontos do polinomio')
ax.plot([x_l, a, x_r], [f(x_l), f(a), f(x_r)], 'ro', label='pontos da funcao')
ax.legend()
plt.show()
