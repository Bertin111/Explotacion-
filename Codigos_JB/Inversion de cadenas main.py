def invertir_cadena(cadena):
    return cadena[::-1]

def main():
    texto = input("Ingrese una cadena de texto para invertir: ")
    texto_invertido = invertir_cadena(texto)
    print(f"La cadena invertida es: {texto_invertido}")

if __name__ == "__main__":
    main()
