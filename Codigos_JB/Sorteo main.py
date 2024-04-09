import random

def sorteo(nombre):
    ganador = random.choice([True, False])
    if ganador:
        mensaje = f"Felicidades, {nombre}! Has ganado el sorteo."
    else:
        mensaje = f"Lo siento, {nombre}. No has ganado en esta ocasión."
    return mensaje

def main():
    nombre = input("Ingrese su nombre para participar en el sorteo: ")
    resultado = sorteo(nombre)
    print(resultado)

if __name__ == "__main__":
    main()
