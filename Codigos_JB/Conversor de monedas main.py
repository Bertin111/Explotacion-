def convertir_dolares_a_euros(dolares):
    euros = dolares * 0.85
    return euros

def main():
    try:
        dolares = float(input("Ingrese la cantidad en dólares a convertir a euros: "))
        euros = convertir_dolares_a_euros(dolares)
        print(f"{dolares} dólares equivalen a {euros} euros.")
    except ValueError:
        print("Error: Ingrese una cantidad válida en dólares.")

if __name__ == "__main__":
    main()
