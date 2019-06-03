def integral(a, b, n, f):
    """Devuelve el resultado de la integral
    definida para el intervalo [a, b] de la
    función f usando la regla de Simpson con
    n + 1 subdivisiones (n debe ser un número
    par).
    """

    def y(k):
        return f(a + k * h)

    h = (b - a) / n

    suma = 0
    for k in range(1, n):
        if k % 2 == 0:
            suma += 2 * y(k)
        else:
            suma += 4 * y(k)
    suma += y(0) + y(n)

    return (h / 3) * suma


def f1(x):
    """Primera función de prueba."""
    return x ** 3


def f2(x):
    """Primera función de prueba."""
    return 4 / (1 + x ** 2)


def main():
    """Ejecuta un par de pruebas de integración
    numérica. Los resultados esperados son
    aproximadamente:

    1/4
    π (pi)
    """
    print(integral(0, 1, 10, f1))
    print(integral(0, 1, 10, f2))


main()
