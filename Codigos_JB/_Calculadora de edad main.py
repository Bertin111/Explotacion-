from datetime import datetime

def calcular_edad(fecha_nacimiento):
    fecha_actual = datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

    if fecha_actual.month < fecha_nacimiento.month or (fecha_actual.month == fecha_nacimiento.month and fecha_actual.day < fecha_nacimiento.day):
        meses = 12 - fecha_nacimiento.month + fecha_actual.month - 1
    else:
        meses = fecha_actual.month - fecha_nacimiento.month

    if fecha_actual.day < fecha_nacimiento.day:
        dias = fecha_actual.day + (30 - fecha_nacimiento.day)
    else:
        dias = fecha_actual.day - fecha_nacimiento.day

    return edad, meses, dias

def main():
    try:
        fecha_str = input("Ingrese su fecha de nacimiento (formato: Año-Mes-Dia): ")
        fecha_nacimiento = datetime.strptime(fecha_str, "%Y-%m-%d")
        edad, meses, dias = calcular_edad(fecha_nacimiento)
        print(f"Su edad es: {edad} años, {meses} meses y {dias} días.")
    except ValueError:
        print("Error: Formato de fecha incorrecto. Utilice el formato YYYY-MM-DD.")

if __name__ == "__main__":
    main()
