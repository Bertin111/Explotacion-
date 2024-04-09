import re

def validar_correo(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(patron, correo):
        return True
    else:
        return False

def main():
    correo = input("Ingrese su correo electrónico: ")
    if validar_correo(correo):
        print("El formato del correo electrónico es correcto.")
    else:
        print("El formato del correo electrónico es incorrecto.")

if __name__ == "__main__":
    main()
