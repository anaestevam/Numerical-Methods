import numpy as np
import matplotlib.pyplot as plt
#coeficientes
b0 = 2
b1 = 4 
ptsx = np.linspace(-5,5,100) #varias abscissas
m = len(ptsx) #tamanho da lista
ptsy = ptsx*b1+ np.random.normal(b0, 1.5, m) #lista com ordenadas somando 1 a 1

numerador = sum(ptsx*ptsy)
denominador = sum(ptsx*ptsx)
#calculando a media das listas
x_mean = np.mean(ptsx)
y_mean = np.mean(ptsy)

a1_calculado = numerador/denominador
a0_calculado = y_mean - a1_calculado*x_mean

print('valor de a1 = ',a1_calculado)
print('valor de a0 = ',a0_calculado)

#Reta de regressão
r = a1_calculado * ptsx + a0_calculado

plt.scatter(ptsx, ptsy, color = 'red')
plt.plot(ptsx, r)
plt.show()
