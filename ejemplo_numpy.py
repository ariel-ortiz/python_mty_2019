"""Ejemplos de operaciones con matrices
usando numpy.
"""

from numpy import array, zeros, transpose
from numpy.random import rand

a = array([[2, 3],
           [1, 0]])

b = array([[1, -1],
           [0, 3]])

z = zeros((5, 10))

x = rand(2, 4)

c = a + b
d = a * 2
e = a * b
f = a @ b
g = transpose(a)

z[0][2] = 1
z[0, 3] = 4

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(z)
print(x)
print(g)
