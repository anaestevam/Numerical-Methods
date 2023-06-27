import numpy as np
import matplotlib.pyplot as plt

# Importar os dados
data = np.loadtxt("precos.txt", delimiter=" ")
cotacao_dolar = data[:, 0]
preco_equipamentos = data[:, 1]

# Calcular a regressão quadrática
n = len(cotacao_dolar)
x = cotacao_dolar
y = preco_equipamentos

sum_x = np.sum(x)
sum_x_squared = np.sum(x**2)
sum_x_cubed = np.sum(x**3)
sum_x_fourth = np.sum(x**4)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x_squared_y = np.sum(x**2 * y)

# Calcular os coeficientes da regressão quadrática
denominator = (n * sum_x_squared * sum_x_fourth - sum_x_cubed**2 - n * sum_x_squared**2 + 2 * sum_x * sum_x_cubed * sum_x_squared - sum_x_fourth * sum_x)
a = (sum_y * sum_x_squared * sum_x_fourth - sum_x * sum_xy * sum_x_fourth - sum_y * sum_x_cubed * sum_x_squared + sum_x_squared_y * sum_x_cubed + sum_xy * sum_x_squared**2 - sum_x_squared_y * sum_x * sum_x_squared) / denominator
b = (-sum_y * sum_x_cubed * sum_x_squared + sum_x * sum_xy * sum_x_squared - sum_xy * sum_x_fourth + sum_x_squared_y * sum_x_cubed + sum_y * sum_x_squared**2 - sum_x_squared_y * sum_x * sum_x_squared) / denominator
c = (sum_y * sum_x_squared * sum_x_fourth - sum_x * sum_xy * sum_x_fourth - sum_x_squared_y * sum_x_cubed + sum_x_squared_y * sum_x_squared - sum_xy * sum_x_squared**2 + sum_x * sum_x_cubed * sum_x_squared) / denominator

# Construir a função quadrática
def funcao_quadratica(x):
    return a * x**2 + b * x + c

# Estimar o preço para o dólar a R$5,50
cotacao_estimada = 5.50
preco_estimado = funcao_quadratica(cotacao_estimada)

# Imprimir os resultados
print("Coeficiente a:", a)
print("Coeficiente b:", b)
print("Coeficiente c:", c)
print("Estimativa de preço para dólar a R$5,50: R$", preco_estimado)

# Plotar os dados e a função quadrática
plt.scatter(cotacao_dolar, preco_equipamentos, label='Dados Originais')
plt.plot(cotacao_dolar, funcao_quadratica(cotacao_dolar), color='red', label='Função Quadrática Ajustada')
plt.xlabel('Cotação do Dólar')
plt.ylabel('Preço dos Equipamentos')
plt.title('Regressão Quadrática')
plt.legend()
plt.show()
