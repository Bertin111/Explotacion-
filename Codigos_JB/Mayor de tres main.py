def encontrar_mayor(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

def main():
    print("Ingrese tres números para determinar cuál es el mayor.")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))

    mayor = encontrar_mayor(num1, num2, num3)
    print(f"El mayor de los tres números es: {mayor}")

if __name__ == "__main__":
    main()
