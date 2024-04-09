from datetime import datetime

def calcular_edad(fecha_nacimiento):
    fecha_actual = datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

def main():
    while True:
        try:
            fecha_str = input("Ingrese su fecha de nacimiento (formato: Año-Mes-Dia): ")
            fecha_nacimiento = datetime.strptime(fecha_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Formato de fecha incorrecto. Intente nuevamente.")

    edad = calcular_edad(fecha_nacimiento)
    print(f"Su fecha de nacimiento es: {fecha_nacimiento.strftime('%Y-%m-%d')}")
    print(f"Su edad actual es: {edad} años.")

if __name__ == "__main__":
    main()
