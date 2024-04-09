def manipulacion_cadenas(cadena):
    cadena_mayusculas = cadena.upper()
    cadena_minusculas = cadena.lower()
    longitud = len(cadena)
    return cadena_mayusculas, cadena_minusculas, longitud

def main():
    texto = input("Ingrese una cadena de texto: ")
    mayusculas, minusculas, longitud = manipulacion_cadenas(texto)

    print("\nCadena en mayúsculas:", mayusculas)
    print("Cadena en minúsculas:", minusculas)
    print("Cantidad de caracteres:", longitud)

if __name__ == "__main__":
    main()
