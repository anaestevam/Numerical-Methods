import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x * np.cos(x) + 1

def f_linha(x):
    return np.cos(x) - x * np.sin(x)

ponto_desconhecido = 1

#intervalo [a,b]
a = 0
b = 6
h = 0.1

#calcula os pontos usando o método de Euler
x = [0]
f_estimada = [ponto_desconhecido]
while x[-1] < b:
    x_new = x[-1] + h
    f_new = f_estimada[-1] + f_linha(x[-1]) * h
    x.append(x_new)
    f_estimada.append(f_new)


x_plot = np.linspace(a, b, 1000)
f_plot = f(x_plot)

plt.plot(x, f_estimada, 'ro', label='Pontos estimados')
plt.plot(x_plot, f_plot, label='f(x)')
plt.plot(0, ponto_desconhecido, 'bo', label='f(0)=1')

plt.legend()
plt.show()
