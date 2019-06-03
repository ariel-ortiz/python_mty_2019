"""Ejemplo de uso matplotlib para
dibujar una gráfica de varias funciones
matemáticas.
"""

from numpy import arange, sin, cos
from numpy.random import rand
from matplotlib.pyplot import plot, show, legend, grid, xlabel, ylabel, title

x = arange(0, 10, 0.1)
y1 = sin(x)
y2 = cos(x)
y3 = rand(len(x))

plot(x, y1, 'r+', label='seno(x)')
plot(x, y2, label='coseno(x)')
plot(x, y3, label='random')

legend()
grid()
xlabel('Eje de las x')
ylabel('Eje de las y')
title('Esto se acabó')

show()
