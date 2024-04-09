def contar_palabras(cadena):
    palabras = cadena.split()
    return len(palabras)

def main():
    texto = input("Ingrese una cadena de texto para contar el número de palabras: ")
    num_palabras = contar_palabras(texto)
    print(f"El número de palabras en la cadena es: {num_palabras}")

if __name__ == "__main__":
    main()
