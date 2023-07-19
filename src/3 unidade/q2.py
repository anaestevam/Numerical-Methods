import numpy as np

def fourier_coefficients(f, T, N):


    #gera pontos no intervalo [0, T]
    t = np.linspace(0, T, 2*N+1, endpoint=False)

    #função nos pontos
    y = f(t)

    #Calcule os coeficientes de Fourier usando numpy.fft.fft
    coefficients = np.fft.fft(y) / (2*N+1)

    #Pegar o coeficiente constante, coeficientes de cosseno e coeficientes de seno
    a0 = coefficients[0].real
    a = coefficients[1:N+1].real
    b = -coefficients[1:N+1].imag

    return a0, a, b
def f(x):
    return x**3 + np.cos(x)

T = 2*np.pi  #Período da função
N = 8  #Num coeficientes

a0, a, b = fourier_coefficients(f, T, N)

print("a0 =", a0)
print("a =", a)
print("b =", b)
