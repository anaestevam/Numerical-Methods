import matplotlib.pyplot as plt

# Passo 1: Importando os dados do arquivo
dados = []
with open('barcos.txt', 'r') as file:
    for line in file:
        valores = line.strip().split()
        vb = float(valores[0])
        tempo = float(valores[1])
        dados.append((vb, tempo))

# Passo 2: Plotando o gráfico com os pontos
velocidades = [x[0] for x in dados]
tempos = [x[1] for x in dados]

plt.scatter(velocidades, tempos)
plt.xlabel('Velocidade Relativa do Barco (vb)')
plt.ylabel('Tempo de Percurso')
plt.title('Gráfico de Tempo de Percurso em Função da Velocidade Relativa do Barco')

# Passo 3: Aplicando regressão polinomial
def regressao_polinomial(X, y, grau):
    n = len(X)
    X_poly = [[X[i]**j for j in range(grau+1)] for i in range(n)]
    coeficientes = gauss_elimination(X_poly, y)
    return coeficientes

def gauss_elimination(A, b):
    n = len(A)
    m = len(A[0])

    for i in range(n):
        if A[i][i] == 0:
            for j in range(i+1, n):
                if A[j][i] != 0:
                    A[i], A[j] = A[j], A[i]
                    b[i], b[j] = b[j], b[i]
                    break

        pivot = A[i][i]
        for j in range(i+1, n):
            factor = A[j][i] / pivot
            A[j][i] = 0
            for k in range(i+1, m):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]

    return x

grau = 2
coeficientes_polinomial = regressao_polinomial(velocidades, tempos, grau)

def funcao_polinomial(vb):
    return sum(coef * vb**i for i, coef in enumerate(coeficientes_polinomial))

plt.plot(velocidades, [funcao_polinomial(v) for v in velocidades], color='red', label='Regressão Polinomial')

# Passo 4: Calculando a função usando o método dos mínimos quadrados
def minimos_quadrados(X, y):
    n = len(X)
    A = [[x + 8, x - 8] for x in X]
    coeficientes = gauss_elimination(A, y)
    return coeficientes

coeficientes_minimos_quadrados = minimos_quadrados(velocidades, tempos)

def funcao_minimos_quadrados(vb):
    return coeficientes_minimos_quadrados[0] * (vb + 8) + coeficientes_minimos_quadrados[1] * (vb - 8)

plt.plot(velocidades, [funcao_minimos_quadrados(v) for v in velocidades], color='green', label='Mínimos Quadrados')

plt.legend()
plt.show()

# Passo 5: Calculando o comprimento estimado do rio
comprimento_estimado = funcao_minimos_quadrados(0)  # Assumindo uma velocidade relativa do barco de 0 km/h

# Passo 6: Estimando o tempo de percurso a 11 km/h
vb = 11

tempo_estimado_polinomial = funcao_polinomial(vb)
tempo_estimado_minimos_quadrados = funcao_minimos_quadrados(vb)

print("Comprimento estimado do rio:", comprimento_estimado)
print("Tempo estimado de percurso (Regressão Polinomial):", tempo_estimado_polinomial)
print("Tempo estimado de percurso (Mínimos Quadrados):", tempo_estimado_minimos_quadrados)
