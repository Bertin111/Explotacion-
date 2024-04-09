def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def main():
    try:
        peso = float(input("Ingrese su peso en kilogramos: "))
        altura = float(input("Ingrese su altura en metros: "))
        imc = calcular_imc(peso, altura)
        print(f"Su Índice de Masa Corporal (IMC) es: {imc:.2f}")
    except ValueError:
        print("Error: Ingrese un valor numérico válido para el peso y la altura.")

if __name__ == "__main__":
    main()
