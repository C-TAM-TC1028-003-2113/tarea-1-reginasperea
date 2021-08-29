def main():
    # escribe tu código abajo de esta línea
    import math
    palabras = int(input("Dame el número de palabras: "))
    if palabras <= 475:
        costo = 60 * 0.90
        print("El costo de la publicación es:", costo)
    else:
        costo = ((math.ceil(palabras / 475)) * 60) * 0.90
        print("El costo de la publicación es:", costo)

if __name__ == '__main__':
    main()
