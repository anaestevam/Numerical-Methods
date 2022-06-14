#Função dada na questão
def f(x):
    return(x**4 - 2.36343*(x**3) - 18.1163*(x**2) + 20.7595*x + 58.8273)
#Derivada da Função
def df(x):
    return(4*(x**4)- 7.09029*(x**2)-36.2326*x + 20.7595)

max_iteracoes = 100 # evita loops infinitos
x0 = 5 #chute inicial
erro = 1

i = 0
while erro > 0.0001 and max_iteracoes > i:
    
    x1 = x0 - (f(x0)/df(x0))
    erro = abs(x1 - x0)
    x0 = x1

    print(f'|{i:2d} | {x1:.10f} |')
    i += 1
