f = lambda x: x**3 + 0.82*(x**2) - 12.4577*x + 4.21686

max_iteracoes = 100 # evita loops infinitos

# valores que delimitam a raíz
a = 2.8
b = 3.4
c = (a + b)/2 # ponto médio

i = 0
while max_iteracoes > i:
    if abs(b - a) < 0.0001:
        break

    c = b - ((b - a)/ (f(b) - f(a)))*f(b)
    a = b
    b = c

    print(f'|{i:2d} | {c:.10f} |')
    i += 1
