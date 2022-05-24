import numpy as np
import matplotlib.pyplot as plt

def bissecao(f,a,b,prec):
    """ Método da bisseção para uma função f no intervalo [a,b]. """
    m = (a+b)/2
    # Se já há precisão suficiente, retornamos o ponto médio do intervalo
    if abs(b - a) < prec: return m
    # Se f(m) == 0, achamos uma raiz exata!
    if f(m) == 0: return m

    # Senão, vamos por recorrência
    if f(m)*f(a) < 0: return bissecao(f,a,m,prec)
    else: return bissecao(f,m,b,prec)


f = lambda x: x**4 - 2.36343*(x**3) - 18.1163*(x**2) + 20.7595*x + 58.8273


