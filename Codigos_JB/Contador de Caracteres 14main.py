def contar_caracteres(texto):
    caracteres_sin_espacios = len(texto.replace(" ", ""))
    return caracteres_sin_espacios

def main():
    texto = input("Ingrese un texto para contar los caracteres (excluyendo espacios en blanco): ")
    num_caracteres = contar_caracteres(texto)
    print(f"El texto tiene {num_caracteres} caracteres (excluyendo espacios en blanco).")

if __name__ == "__main__":
    main()
