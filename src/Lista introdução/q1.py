import math

vlr = 10
resultado = math.sqrt(vlr)
x = 1

for i in range(10):
    x = x + vlr/(2*x) - x/2
    print(x)
    print(f'\tErro absoluto: {abs(resultado-x)}')
    print(f'\tErro relativo: {abs(resultado-x)/resultado}')

#O erro absoluto Ea = a diferenca entre o vlr exato e o vlr aproximado em modulo
#O erro relativo Er = a divisao do erro absoluto e o vlr exato
