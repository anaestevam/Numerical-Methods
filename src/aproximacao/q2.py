import numpy as np
import matplotlib.pyplot as plt


caminho_arquivo = "pesos.txt"

data = np.loadtxt(caminho_arquivo, delimiter=" ")
altura = data[:, 0]
peso = data[:, 1]

n = len(altura)
sum_x = np.sum(altura)
sum_y = np.sum(peso)
sum_x_quadrado = np.sum(altura ** 2)
sum_xy = np.sum(altura * peso)

#     |  n∑xiyi - ∑x∑y
# B = |  --------------
#     |   n∑x² - (∑x)²
coeficiente_angular = (n * sum_xy - sum_x * sum_y) / (n * sum_x_quadrado - sum_x ** 2)
#     |    ∑y - B * ∑x
# A = |  --------------
#     |         n
coeficiente_linear = (sum_y - coeficiente_angular * sum_x) / n

altura_estimada = 2.10

# y = A + B * X
peso_estimado = coeficiente_linear + coeficiente_angular * altura_estimada

reta = coeficiente_linear + coeficiente_angular * altura

print(f'O peso estimado para uma altura de 2m10cm é aproximadamente {peso_estimado:.2f} kg.')

plt.scatter(altura, peso, color='b', label='Dados')
plt.plot(altura, reta, color='r', label='Função linear')
plt.xlabel('Altura (m)')
plt.ylabel('Peso (kg)')
plt.legend()
plt.show()

