import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("precos.txt", delimiter=" ")
velocidades = data[:, 0]
tempos = data[:, 1]

def eliminacao_gauss(A, b, pivotamento_parcial=False):
    n = len(A)
    x = np.zeros(n)

    for i in range(n):
        if pivotamento_parcial:
            max_row = i
            for j in range(i + 1, n):
                if abs(A[j, i]) > abs(A[max_row, i]):
                    max_row = j
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]

        pivot = A[i, i]
        for j in range(i + 1, n):
            factor = A[j, i] / pivot
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    x[n-1] = b[n-1] / A[n-1, n-1]
    for i in range(n - 2, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

    return x
    
def regressao_polinomial(X, y, grau):
    n = len(X)
    X_poly = [[X[i]**j for j in range(grau+1)] for i in range(n)]
    coeficientes = eliminacao_gauss(X_poly, y)
    return coeficientes

grau = 2
coeficientes_polinomial = regressao_polinomial(velocidades, tempos, grau)

def funcao_polinomial(vb):
    return sum(coef * vb**i for i, coef in enumerate(coeficientes_polinomial))

#Passo 4: Calculando a função usando o método dos mínimos quadrados
def minimos_quadrados(X, y):
    n = len(X)
    A = [[x + 8, x - 8] for x in X]
    coeficientes = eliminacao_gauss(A, y)
    return coeficientes

coeficientes_minimos_quadrados = minimos_quadrados(velocidades, tempos)

def funcao_minimos_quadrados(vb):
    return coeficientes_minimos_quadrados[0] * (vb + 8) + coeficientes_minimos_quadrados[1] * (vb - 8)


#Passo 5: Calculando o comprimento estimado do rio
comprimento_estimado = funcao_minimos_quadrados(0)  # Assumindo uma velocidade relativa do barco de 0 km/h

#Passo 6: Estimando o tempo de percurso a 11 km/h
vb = 11

tempo_estimado_polinomial = funcao_polinomial(vb)
tempo_estimado_minimos_quadrados = funcao_minimos_quadrados(vb)

plt.scatter(velocidades, tempos)
plt.xlabel('Velocidade relativa do barco (vb)')
plt.ylabel('Tempo de percurso')
plt.title('Gráfico de tempo em função da velocidade do barco')
plt.plot(velocidades, [funcao_polinomial(v) for v in velocidades], color='red', label='Regressão Polinomial')
# plt.plot(velocidades, [funcao_minimos_quadrados(v) for v in velocidades], color='green', label='Mínimos Quadrados')

print("Comprimento estimado do rio:", comprimento_estimado)
print("Tempo estimado de percurso (Regressão Polinomial):", tempo_estimado_polinomial)
print("Tempo estimado de percurso (Mínimos Quadrados):", tempo_estimado_minimos_quadrados)

plt.legend()
plt.show()