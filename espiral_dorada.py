from math import sqrt
from turtle import circle, done

def chicharronera(a, b, c):
    """Devuelve el valor de x para la ecuación cuadrática
    de tipo:  ax**2 + bx + c = 0
    """
    return (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)

x = chicharronera(1, 1, -1)
PHI = 1 / x
print(PHI)

radio = 10
for i in range(8):
    circle(radio, 90)
    radio *= PHI
    
done()
    