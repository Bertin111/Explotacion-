def numeros_pares_impares():
    numeros_pares = []
    numeros_impares = []
    
    for num in range(1, 41):  # Rango del 1 al 40 (20 pares y 20 impares)
        if num % 2 == 0:
            numeros_pares.append(num)
        else:
            numeros_impares.append(num)
    
    return numeros_pares, numeros_impares

def main():
    pares, impares = numeros_pares_impares()
    
    print("Los primeros 20 números pares son:")
    print(pares)
    
    print("\nLos primeros 20 números impares son:")
    print(impares)

if __name__ == "__main__":
    main()
