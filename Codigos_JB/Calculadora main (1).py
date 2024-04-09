def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"

def main():
    print("Bienvenido a la Calculadora Básica ")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Seleccione una operación (1/2/3/4): ")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        resultado = suma(num1, num2)
    elif opcion == '2':
        resultado = resta(num1, num2)
    elif opcion == '3':
        resultado = multiplicacion(num1, num2)
    elif opcion == '4':
        resultado = division(num1, num2)
    else:
        print("Opción no válida")
        return

    print(f"El resultado de la operación es: {resultado}")

if __name__ == "__main__":
    main()