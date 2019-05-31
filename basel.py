def basel(n):
    """Calcula y devuelve la serie de basel de n.
    """
    suma = 0
    for k in range(1, n + 1):
        suma += 1 / (k ** 2)
    return suma

def main():
    """Imprime basel(n) para n = 10, 100, 1000, ... 10**7.
    """
    for exponente in range(1, 8):
        n = 10 ** exponente
        resultado = basel(n)
        print(f'{n:>10} {resultado:15.10f}')
        
main()