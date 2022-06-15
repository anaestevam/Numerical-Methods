import cv2
import numpy as np
import math
def bilinear_interpolation(x, y, points):
    
    points = sorted(points) #ordenar os pontos por x, depois por y
    (x1, y1, q11), (_x1, y2, q12), (x2, _y1, q21), (_x2, _y2, q22) = points

    if x1 != _x1 or x2 != _x2 or y1 != _y1 or y2 != _y2:
        raise ValueError('os pontos não formam um retângulo')
    if not x1 <= x <= x2 or not y1 <= y <= y2:
        raise ValueError('(x, y) não estão dentro do retângulo')

    return (q11 * (x2 - x) * (y2 - y) +
            q21 * (x - x1) * (y2 - y) +
            q12 * (x2 - x) * (y - y1) +
            q22 * (x - x1) * (y - y1)
           ) / ((x2 - x1) * (y2 - y1) + 0.0)
L = 54.4786674627
C = 17.0470721369

m = 0.016667
#execute os seguintes comandos no console

#n = [(54.5,17.041667,31.993),(54.5,17.083333,31.911),(54.458333,17.041667,31.945),(54.458333,17.083333,31.866)]

#bilinear_interpolation(54.4786674627, 17.0470721369, n)
