import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

def main():
    try:
        longitud = int(input("Ingrese la longitud de la contraseña que desea generar: "))
        if longitud <= 0:
            raise ValueError("La longitud de la contraseña debe ser mayor que cero.")
        contraseña_generada = generar_contraseña(longitud)
        print(f"Contraseña generada: {contraseña_generada}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
