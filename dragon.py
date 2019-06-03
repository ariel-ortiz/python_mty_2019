from turtle import fd, lt, rt, done, speed, ht


def invierte(lst):
    """Devuelve una nueva lista en donde se intercambia
    cada ocurrencia en lst de 'I' por 'D' y viceversa.
    """
    resultado = []
    for c in lst:
        if c == 'I':
            resultado.append('D')
        else:
            resultado.append('I')
    return resultado


def curva(n):
    """Devuelve una lista de caracteres con los giros
    requeridos para dibujar la curva de dragón de orden
    n. La letra 'I' significa girar a la izquierda,
    mientras que la letra 'D' significa girar a la
    derecha.
    """
    resultado = []
    for orden in range(n):
        volteado = resultado[::-1]
        volteado = invierte(volteado)
        resultado = resultado + ['I'] + volteado
    return resultado


def dragon(n, lado):
    """Dibuja una curva de dragón de orden n en donde
    cada segmento de la curva es de longitud lado.
    """
    fd(lado)
    for giro in curva(n):
        if giro == 'I':
            lt(90)
        else:
            rt(90)
        fd(lado)


def main():
    """Dibuja una curva de dragón de orden 10
    y de lado 10.
    """
    ht()
    speed(0)
    dragon(10, 10)
    done()


main()
