import numpy as np
import matplotlib.pyplot as plt

def f(x):
    b0+b1*x
b1 = 4 #coeficientes
ptsx = np.linspace(-5,5,100) #varias abcissas
m = len(ptsx) #tamanho da lista
ptsy = ptsx*b1+ np.random.normal(0, 2, m) #lista com ordenadas somando 1 a 1

numerador = sum(ptsx*ptsy)
denominador = sum(ptsx*ptsx)
b1_calculado = numerador/denominador
print(b1_calculado)

plt.scatter(ptsx, ptsy)
plt.plot(ptsx, b1_calculado*ptsx)
plt.show()

