f = lambda x: x**4 - 2.36343*(x**3) - 18.1163*(x**2) + 20.7595*x + 58.8273

max_iteracoes = 100 # evita loops infinitos

# valores que delimitam a raíz
a = -4
b = 4
m = (f(b) - f(a))/(b-a)
c = a - f(a)/m

i = 0
while abs(f(c)) > 0.0001 and max_iteracoes > i:
    if abs(b - a) < 0.0001:
        break

    if f(c)*f(a) > 0:
        a = c
    else:
        b = c
    m = (f(b) - f(a))/(b-a)
    c = a - f(a)/m

    print(f'|{i:2d} | {c:.10f} | {f(c):.10f}')
    i += 1 
