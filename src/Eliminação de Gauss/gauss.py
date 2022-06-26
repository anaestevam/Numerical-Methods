import os
import sympy as sp # baixar biblioteca: pip install sympy
import numpy as np

# ======================================================================
# eliminação dew gauss


#forma matriz aumentada
def matrix_representation(system, syms):
    #extrair coeficientes de equação e constante
    a, b = sp.linear_eq_to_matrix(system, syms)

    #inserir valores de tamanho à direita na matriz de coeficientes
    return np.asarray(a.col_insert(len(syms), b), dtype=np.float32)


# escrever linhas em forma escalonada de linha
def upper_triangular(M):
    #mover todos os zeros para o buttom da matriz
    M = np.concatenate((M[np.any(M != 0, axis=1)], M[np.all(M == 0, axis=1)]), axis=0)

    #iterar sobre as linhas da matriz
    for i in range(0, M.shape[0]):

        #inicializar iterador de troca de linha
        j = 1

        # selecione o valor do pivô
        pivot = M[i][i]

        # encontre o próximo coeficiente principal diferente de zero
        while pivot == 0 and i + j < M.shape[0]:
            # executar operação de troca de linha
            M[[i, i + j]] = M[[i + j, i]]

            # iterador de troca de linha incremental
            j += 1

            # obter novo pivô
            pivot = M[i][i]

        # se o pivô for zero, as linhas restantes serão todas zeros
        if pivot == 0:
            # retornar matriz triangular superior
            return M

        # extrair linha
        row = M[i]

        # obter 1 ao longo da diagonal
        M[i] = row / pivot

        # iterate over remaining rows
        for j in range(i + 1, M.shape[0]):
            # subtract current row from remaining rows
            M[j] = M[j] - M[i] * M[j][i]

    # retornar matriz triangular superior
    return M


def backsubstitution(M, syms):
    # índice de variável simbólica
    for i, row in reversed(list(enumerate(M))):
        # criar equação simbólica
        eqn = -M[i][-1]
        for j in range(len(syms)):
            eqn += syms[j] * row[j]

        # resolva a expressão simbólica e armazene a variável
        syms[i] = sp.solve(eqn, syms[i])[0]

    # retornar lista de variáveis ​​avaliadas
    return syms


def validate_solution(system, solutions, tolerance=1e-6):
    # iterar sobre cada equação
    for eqn in system:
        # a equação assert está resolvida
        assert eqn.subs(solutions) < tolerance


# resolver o sistema usando funções internas numpy
def linalg_solve(system, syms):
    # converter lista de equações para a forma de matriz
    M, c = sp.linear_eq_to_matrix(system, syms)

    # formar matriz aumentada - converter matrizes sympy em matrizes numpy e concatenar
    M, c = np.asarray(M, dtype=np.float32), np.asarray(c, dtype=np.float32)

    # resolver sistema de equações
    return np.linalg.solve(M, c)


if __name__ == '__main__':

    # variáveis ​​simbólicas
    x1, x2, x3 = sp.symbols('x1 x2 x3')
    symbolic_vars = [x1, x2, x3]

    # definir sistema de equações
    equations = [x1 - 2 * x2 - x3 - 6, 2 * x1 + 2 * x2 - x3 - 1, -x1 - x2 + 2 * x3 - 1]

    # exibir equações
    [print(eqn) for eqn in equations]

    # obter representação de matriz aumentada
    augmented_matrix = matrix_representation(system=equations, syms=symbolic_vars)
    print('\matriz aumentada:\n', augmented_matrix)

    # gerar forma de matriz triangular superior
    upper_triangular_matrix = upper_triangular(augmented_matrix)
    print('\matriz triangular nupper:\n', upper_triangular_matrix)

    # remover zero linhas
    backsub_matrix = upper_triangular_matrix[np.any(upper_triangular_matrix != 0, axis=1)]

    # inicializar solução numérica
    numeric_solution = np.array([0., 0., 0.])

    # afirmar que o número de linhas na matriz é igual ao número de variáveis ​​desconhecidas
    if backsub_matrix.shape[0] != len(symbolic_vars):
        print('sistema dependente. número infinito de solucoes')
    elif not np.any(backsub_matrix[-1][:len(symbolic_vars)]):
        print('sistema inconsistente. sem solucao..')
    else:
        # backsubstitute para resolver variáveis
        numeric_solution = backsubstitution(backsub_matrix, symbolic_vars)
        print(f'\nsolucoes:\n{numeric_solution}')
