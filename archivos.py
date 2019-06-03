def main():
    """Muestra cómo leer y escribir un arhivo de texto."""

    # Lectura de archivo.
    with open('archivos.py') as archivo:
        for linea in archivo:
            print(linea, end='')

    # Escritura de archivo.
    with open('salida.txt', 'w') as arch:
        print('Hola', file=arch)
        print('Fin.', file=arch)


main()
