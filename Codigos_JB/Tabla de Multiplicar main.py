def tabla_multiplicar(numero):
    print("Tabla de multiplicar del:", numero)
    contador = 1
    while contador <= 10:
        resultado = numero * contador
        print(numero, "x", contador, "=", resultado)
        contador += 1

def main():
    try:
        numero = int(input("Ingrese un número para generar su tabla de multiplicar: "))
        tabla_multiplicar(numero)
    except ValueError:
        print("Error: Ingrese un número entero válido.")

if __name__ == "__main__":
    main()
