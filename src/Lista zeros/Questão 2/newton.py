#Função dada na questão
def f(x):
    return(x**3 + 0.82*(x**2) - 12.4577*x + 4.21686)
#Derivada da Função
def df(x):
    return(3*x**2 + 1.64*x - 12.4577)

max_iteracoes = 100 # evita loops infinitos
x0 = 1.2 #chute inicial
erro = 1

i = 0
while erro > 0.0001 and max_iteracoes > i:
    
    x1 = x0 - (f(x0)/df(x0))
    erro = abs(x1 - x0)
    x0 = x1

    print(f'|{i:2d} | {x1:.10f} |')
    i += 1
