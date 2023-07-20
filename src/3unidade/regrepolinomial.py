import numpy as np
import matplotlib.pyplot as plt

def regressaopolinomial(x: list[float],y: list[float],k: int)->list[float]:
    n = len(x)
    if n <= k:
        raise ValueError('O número de pontos deve ser maior que o grau k do polinômio')
    somas = {}
    somas[0] = n
    for n in range(1,2 * k+1):
        somas[n] = sum(xi ** n for xi in x)

    A = []
    B = []
    for i in range(k + 1):
        row = []
        for j in range(k + 1):
            row.append(somas[i + j])
        A.append(row)
        if i == 0:
            B.append(sum(y))
        else:
            B.append(sum(xi ** i * yi for xi, yi in zip(x,y)))

    return np.linalg.solve(A,B)
    
    
x = np.linspace(-2, 2, 100)
y = [2 + 0.5 * xi + 2.1 * xi ** 2 + np.pi * np.random.random() for xi in x]
k = 2
coefs = regressaopolinomial(x, y, k)
print(f'{coefs=}')

def p(x, coefs):
    return coefs[0] + sum(ci * x ** i for i, ci in enumerate(coefs[1:], 1))

t = np.linspace(min(x), max(x), 100)
pt = [p(ti, coefs) for ti in t]

plt.plot(t, pt)
plt.scatter(x,y)
plt.show()
