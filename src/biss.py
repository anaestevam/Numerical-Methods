import numpy as np

# Definindo a função
def f(x):
    return x**4 - 2.36343*(x**3) - 18.1163*(x**2) + 20.7595*x + 58.8273

# Definindo o ponto médio
def ponto_medio(x, y):
    return (x + y)/2

# Implementando o método de Newton
def met_Newton(a, b,tol,N):
    print('\n\n*** IMPLEMENTAÇÃO DO MÉTODO DE NEWTON ***')
    n = 1
    aux = 1
    condicao = True
    while condicao:
        if ponto_medio(a, b) == 0.0:
            print('Erro - Divisão por zero!')
            break
        
        xr = x0 - f(x0)/ponto_medio(a, b)
        print('Iteração %d, xr = %0.6f and f(xr) = %0.6f' % (n, xr, f(xr)))
        x0 = xr
        n += 1
        
        if n > N:
            aux = 0
            break
        
        condicao = abs(f(xr)) > tol
    
    if aux==1:
        print('\n A Raiz desejada é : %0.6f' % xr)
    else:
        print('\n Não Convergente.')


# Dados de entrada
a = float(input('Intervalo (a) : '))
b = float(input('Intervalo (b) : '))
tol = float(input('Tolerância : '))
N = int(input('Número máximo de iterações (N) : '))


# nicialiando o método de Newton
met_Newton(a, b, tol, N)
