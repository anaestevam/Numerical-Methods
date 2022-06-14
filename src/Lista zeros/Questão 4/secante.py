f = lambda x: x**4 - 2.36343*(x**3) - 18.1163*(x**2) + 20.7595*x + 58.8273

max_iteracoes = 100 # evita loops infinitos

# valores que delimitam a raíz
a = -3.2
b = 1.5
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
