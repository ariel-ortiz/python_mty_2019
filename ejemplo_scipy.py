"""Ejemplo de integración numérica usando
la función quad de scipy.
"""

from scipy.integrate import quad


def f1(x):
    """Primera función de prueba."""
    return x ** 3


def f2(x):
    """Segunda función de prueba."""
    return 4 / (1 + x ** 2)


# Resultado aproximado: 1/4
r, e = quad(f1, 0, 1)
print(r)

# Resultado aproximado: π (pi)
r, e = quad(f2, 0, 1)
print(r)
