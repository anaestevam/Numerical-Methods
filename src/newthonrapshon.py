def f(x):
    return(x**4 - 2.36343*(x**3) - 18.1163*(x**2) + 20.7595*x + 58.8273)

def fi(x):
    return(4*(x**4)- 7.09029*(x**2)-36.2326*x + 20.7595)

def hata(x1,x2):
    return((x1-x2)/x1)

x1 = int(input("insira um valor inicial: "))

for i in range(5):
    x2 = x1 - f(x1)/fi(x1)
    print(x1, x2, hata(x2,x1))
    x1 = x2

