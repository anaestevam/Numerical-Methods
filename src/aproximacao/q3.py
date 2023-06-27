import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("precos.txt", delimiter=" ")
cotacao_dolar = data[:, 0]
preco_equipamentos = data[:, 1]

n = len(cotacao_dolar)
x = cotacao_dolar
y = preco_equipamentos

sum_x = np.sum(x)
sum_x_quadrado = np.sum(x**2)
sum_x_cubo = np.sum(x**3)
sum_x_quarta = np.sum(x**4)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x_quadrado_y = np.sum(x**2 * y)

denominator = (n * sum_x_quadrado * sum_x_quarta - sum_x_cubo**2 - n * sum_x_quadrado**2 + 2 * sum_x * sum_x_cubo * sum_x_quadrado - sum_x_quarta * sum_x)
a = (sum_y * sum_x_quadrado * sum_x_quarta - sum_x * sum_xy * sum_x_quarta - sum_y * sum_x_cubo * sum_x_quadrado + sum_x_quadrado_y * sum_x_cubo + sum_xy * sum_x_quadrado**2 - sum_x_quadrado_y * sum_x * sum_x_quadrado) / denominator
b = (-sum_y * sum_x_cubo * sum_x_quadrado + sum_x * sum_xy * sum_x_quadrado - sum_xy * sum_x_quarta + sum_x_quadrado_y * sum_x_cubo + sum_y * sum_x_quadrado**2 - sum_x_quadrado_y * sum_x * sum_x_quadrado) / denominator
c = (sum_y * sum_x_quadrado * sum_x_quarta - sum_x * sum_xy * sum_x_quarta - sum_x_quadrado_y * sum_x_cubo + sum_x_quadrado_y * sum_x_quadrado - sum_xy * sum_x_quadrado**2 + sum_x * sum_x_cubo * sum_x_quadrado) / denominator

def funcao_quadratica(x):
    return a * x**2 + b * x + c

cotacao_estimada = 5.50
preco_estimado = funcao_quadratica(cotacao_estimada)

print("Coeficiente a:", a)
print("Coeficiente b:", b)
print("Coeficiente c:", c)
print("Estimativa de preço para dólar a R$5,50: R$", preco_estimado)

plt.scatter(cotacao_dolar, preco_equipamentos, label='Dados Originais')
plt.plot(cotacao_dolar, funcao_quadratica(cotacao_dolar), color='red', label='Função Quadrática Ajustada')
plt.xlabel('Cotação do Dólar')
plt.ylabel('Preço dos Equipamentos')
plt.title('Regressão Quadrática')
plt.legend()
plt.show()
