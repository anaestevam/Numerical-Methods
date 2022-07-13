import numpy as np
import matplotlib.pyplot as plt

a1 = 4 #coeficientes
ptsx = np.linspace(-5,5,100) #varias abcissas
m = len(ptsx) #tamanho da lista
ptsy = ptsx*a1+ np.random.normal(0, 1.5, m) #lista com ordenadas somando 1 a 1

numerador = sum(ptsx*ptsy)
denominador = sum(ptsx*ptsx)
a1_calculado = numerador/denominador
print(a1_calculado)

plt.scatter(ptsx, ptsy)
plt.plot(ptsx, a1_calculado*ptsx)
plt.show()

