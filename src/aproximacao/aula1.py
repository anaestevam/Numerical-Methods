import numpy as np
import matplotlib.pyplot as plt

def phi0(x):
    return np.sin
def phi1(x):
    return 2*np.power(x,2)

caminho_arquivo = "barcos.txt"

data = np.loadtxt(caminho_arquivo, delimiter=" ")
pts = data[:, 0]
r = data[:, 1]

b = (sum(phi0(pts)*phi0(pts)))
c = (sum(phi0(pts)*phi1(pts)))
d = (sum(phi1(pts)*phi0(pts)))
e = (sum(phi1(pts)*phi1(pts)))
f = (sum(r*phi0(pts)))
g = (sum(r*phi1(pts)))

a = np.linalg.solve(np.array([[b, c],[d, e]]), np.array([[f],[g]]))

plt.scatter(pts,r)
x = np.linspace(8,11,100)
plt.plot(x,a[0]*phi0(x)+a[1]*phi1(x))
plt.plot(pts)
plt.show()

#print(np.sum(phi0(pts)*))