
#funcao f(x) da qual vamos extrair as raizes
def f(x):
	return x**3 + 0.82*(x**2) - 12.4577*x + 4.21686

#1a derivada da funcao f(x)
def df(x):
	return(3*x**2 + 1.64*x - 12.4577)

def ponto_medio(x, y):
    return (x + y)/2

#metodo da bissecao
def bissecao(a, b):
    max_iteracoes = 1000 # evita loops infinitos
    n = 0
    result = -1
    erro = 0.0001
    #intervalo = {'a': -4.3, 'b': 4.0}
    #a = intervalo['a']; b = intervalo['b'] # variaveis para o intervalo
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

#metodo de Newton
def newton(x0):
    max_iteracoes = 100 # evita loops infinitos
    #x0 = 1.2 #chute inicial
    erro = 1

    i = 0
    while erro > 0.0001 and max_iteracoes > i:
        
        x1 = x0 - (f(x0)/df(x0))
        erro = abs(x1 - x0)
        x0 = x1

        print(f'|{i:2d} | {x1:.10f} |')
        i += 1

#metodo da secante
def secante(a, b):
    f = lambda x: x**3 + 0.82*(x**2) - 12.4577*x + 4.21686

    max_iteracoes = 100 # evita loops infinitos

    # valores que delimitam a raíz
    #a = 2.8
    #b = 3.4
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

#metodo regula falsi
def regulaFalsi(a, b):
    f = lambda x: x**3 + 0.82*(x**2) - 12.4577*x + 4.21686

    max_iteracoes = 100 # evita loops infinitos

    # valores que delimitam a raíz
    #a = 0
    #b = 1
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


#coloque em ... os valores iniciais
print("Bissecao:")
print(bissecao(-4.3, 4.0))
print("Newton:")
print(newton(1.2))
print("Secante:")
print(secante(2.8, 3.4))
print("Regula Falsi:")
print(regulaFalsi(0, 1))
