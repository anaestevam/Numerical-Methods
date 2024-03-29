def f(x):
    return x**3 + 0.82*(x**2) - 12.4577*x + 4.21686
intervalo = {'a': -4.3, 'b': 4.0}

def ponto_medio(x, y):
    return (x + y)/2

max_iteracoes = 1000 # evita loops infinitos
n = 0
result = -1
erro = 0.0001

a = intervalo['a']; b = intervalo['b'] # variaveis para o intervalo
print(f'   I | Intervalo a | Intervalo b | Valor médio c |     f(c)   |')

while n < max_iteracoes and abs(a - b) > erro:
    c = ponto_medio(a, b)
    fc = f(c)
    # encontrado a raiz
    if fc == 0:
        print(f' {n:3d} | {a:11f} | {b:11f} | {c:13f} | {fc:10f} |')
        result = c
        break
    n += 1

    # busca binária no intervalo
    if f(a)*fc < 0:
        b = c
    else:
        a = c

    print(f' {n:3d} | {a:11f} | {b:11f} | {c:13f} | {fc:10f} |')

print(f'O valor da raiz é {c}')
