def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_a_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def kelvin_a_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def main():
    try:
        print("Seleccione la conversión que desea realizar:")
        print("1. Celsius a Fahrenheit")
        print("2. Fahrenheit a Celsius")
        print("3. Celsius a Kelvin")
        print("4. Kelvin a Celsius")
        opcion = int(input("Ingrese el número de la opción deseada: "))

        if opcion == 1:
            celsius = float(input("Ingrese la temperatura en grados Celsius: "))
            fahrenheit = celsius_a_fahrenheit(celsius)
            print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit.")
        elif opcion == 2:
            fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
            celsius = fahrenheit_a_celsius(fahrenheit)
            print(f"{fahrenheit} grados Fahrenheit equivalen a {celsius} grados Celsius.")
        elif opcion == 3:
            celsius = float(input("Ingrese la temperatura en grados Celsius: "))
            kelvin = celsius_a_kelvin(celsius)
            print(f"{celsius} grados Celsius equivalen a {kelvin} Kelvin.")
        elif opcion == 4:
            kelvin = float(input("Ingrese la temperatura en Kelvin: "))
            celsius = kelvin_a_celsius(kelvin)
            print(f"{kelvin} Kelvin equivalen a {celsius} grados Celsius.")
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")

if __name__ == "__main__":
    main()
