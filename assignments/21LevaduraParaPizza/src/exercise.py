def main():
    # escribe tu código abajo de esta línea
    import math
    harina = float(input("Dame la harina en gramos: "))
    levadura = float(math.ceil((harina/1000) * 50))
    print("Necesitas estos gramos de levadura:", levadura)

if __name__ == '__main__':
    main()
