import math

def area_perimetro_circulo(radio):
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    return area, perimetro

def area_perimetro_cuadrado(lado):
    area = lado ** 2
    perimetro = 4 * lado
    return area, perimetro

def area_perimetro_rectangulo(base, altura):
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro

def main():
    radio = float(input("Ingrese el radio del círculo: "))
    lado_cuadrado = float(input("Ingrese el lado del cuadrado: "))
    base_rectangulo = float(input("Ingrese la base del rectángulo: "))
    altura_rectangulo = float(input("Ingrese la altura del rectángulo: "))

    area_circulo, perimetro_circulo = area_perimetro_circulo(radio)
    area_cuadrado, perimetro_cuadrado = area_perimetro_cuadrado(lado_cuadrado)
    area_rectangulo, perimetro_rectangulo = area_perimetro_rectangulo(base_rectangulo, altura_rectangulo)

    print(f"\nCírculo:")
    print(f"Área: {area_circulo}, Perímetro: {perimetro_circulo}")

    print(f"\nCuadrado:")
    print(f"Área: {area_cuadrado}, Perímetro: {perimetro_cuadrado}")

    print(f"\nRectángulo:")
    print(f"Área: {area_rectangulo}, Perímetro: {perimetro_rectangulo}")

if __name__ == "__main__":
    main()
