def reemplazar_palabras_prohibidas(texto, palabras_prohibidas):
    for palabra in palabras_prohibidas:
        texto = texto.replace(palabra, '*' * len(palabra))
    return texto

def main():
    texto = input("Ingrese un texto: ")
    palabras_prohibidas = input("Ingrese una lista de palabras prohibidas separadas por comas: ").split(',')
    texto_modificado = reemplazar_palabras_prohibidas(texto, palabras_prohibidas)
    print("Texto modificado:")
    print(texto_modificado)

if __name__ == "__main__":
    main()
