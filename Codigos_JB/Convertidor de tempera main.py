def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    print("Bienvenido al Convertidor de Temperaturas ")
    print("1. Convertir de Celsius a Fahrenheit")
    print("2. Convertir de Fahrenheit a Celsius")
    
    option = input("Seleccione una opción (1/2): ")
    
    if option == '1':
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
    elif option == '2':
        fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} grados Fahrenheit son {celsius} grados Celsius.")
    else:
        print("Opción no válida. Por favor, seleccione 1 o 2.")

if __name__ == "__main__":
    main()