import numpy as np

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

def residuo_norma(A, b, x):
    b_calculado = np.dot(A, x)
    residual = b - b_calculado
    norma = np.linalg.norm(residual)
    return norma

def refinamento(A, b, x, iterations):
    n = len(A)
    for _ in range(iterations):
        r = b - np.dot(A, x)
        delta_x = np.linalg.solve(A, r)
        x += delta_x
    return x

def read_input_file(filename):
    with open(filename, 'r') as file:
        n = int(file.readline())
        A = np.zeros((n, n))
        b = np.zeros(n)
        for i in range(n):
            line = file.readline().split()
            for j in range(n):
                A[i, j] = float(line[j])
            b[i] = float(line[n])
    return A, b

# def write_output_file(filename, x, norm):
#    with open(filename, 'w') as file:
#        file.write("Solução:\n")
#        for i in range(len(x)):
#            file.write(f"x{i+1} = {x[i]}\n")
#        file.write(f"Residuo normal: {norm}\n")

A, b = read_input_file('m1.in')

opcao = int(input("Escolha a opção de pivotamento:\n1. Sem pivotamento parcial\n2. Com pivotamento parcial\n"))
refinamento_iteracao = int(input("Digite o número de iterações para refinamento: "))

if opcao == 1:
    x = eliminacao_gauss(A, b)
elif opcao == 2:
    x = eliminacao_gauss(A, b, pivotamento_parcial=True)
else:
    print("Escolha inválida.")

x_refined = refinamento(A, b, x, refinamento_iteracao)

residual_norm_inicial = residuo_norma(A, b, x)
residual_norm_refined = residuo_norma(A, b, x_refined)

#write_output_file('output/m1.out', x_refined, residual_norm_refined)

# print("Resultado escrito no arquivo 'output/m1.out'.")
print("Norma do vetor residual antes do refinamento:", residual_norm_inicial)
print("Norma do vetor residual após o refinamento:", residual_norm_refined)
