import numpy as np
import matplotlib.pyplot as plt

# Fornecer o caminho local do arquivo "pesos.txt"
caminho_arquivo = "pesos.txt"

# Importar os dados
data = np.loadtxt(caminho_arquivo, delimiter=" ")
altura = data[:, 0]
peso = data[:, 1]

# Calcular as somas necessárias para a regressão linear
n = len(altura)
sum_x = np.sum(altura)
sum_y = np.sum(peso)
sum_x_squared = np.sum(altura ** 2)
sum_xy = np.sum(altura * peso)

# Calcular os coeficientes da regressão linear
m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
c = (sum_y - m * sum_x) / n

plt.scatter(altura, peso, color='b', label='Dados')
plt.plot(altura, m * altura + c, color='r', label='Função linear')
plt.xlabel('Altura (m)')
plt.ylabel('Peso (kg)')
plt.legend()
plt.show()

# Estimar o peso para uma altura de 2m10cm (2,10m)
altura_estimada = 2.10
peso_estimado = m * altura_estimada + c
print(f'O peso estimado para uma altura de 2m10cm é de aproximadamente {peso_estimado:.2f} kg.')
