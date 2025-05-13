# mediciones.py

from datetime import datetime

def gestionar_mediciones(mediciones, parcelas, sensores, sensores_en_parcelas):
    """
    Submenú para registrar y visualizar mediciones.
    """

    opcion = ''
    while opcion != "3":
        print("\n---- GESTIÓN DE MEDICIONES ----")
        print("1. Ver Mediciones Registradas")
        print("2. Registrar Nueva Medición")
        print("3. Volver al Menú Principal")
        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            # Mostrar todas las mediciones ordenadas por fecha y hora
            if not mediciones:
                print("No hay mediciones registradas.")
            else:
                print("\nMediciones registradas:")
                # Ordenar las mediciones por fecha y hora
                for m in sorted(mediciones, key=lambda x: x["fecha_hora"]):
                    print(f"Parcela {m['parcela']} - Sensor {m['sensor']} - {m['valor']} {m['unidad']} - {m['fecha_hora'].strftime('%d/%m/%Y %H:%M')}")

        elif opcion == "2":
            # Registrar una nueva medición manualmente
            parcela = int(input("Ingrese número de parcela: "))

            if parcela not in sensores_en_parcelas or not sensores_en_parcelas[parcela]:
                print("La parcela no tiene sensores instalados.")
                continue

            print(f"Sensores instalados en Parcela {parcela}: {sensores_en_parcelas[parcela]}")
            sensor = int(input("Ingrese número de sensor: "))

            if sensor not in sensores_en_parcelas[parcela]:
                print("El sensor ingresado no está instalado en esa parcela.")
                continue

            valor = input("Ingrese valor de la medición (ej: 42): ")
            unidad = input("Ingrese unidad (ej: %, °C, pH): ")

            # Pedir fecha y hora hasta que se ingrese correctamente
            while True:
                fecha_hora_input = input("Ingrese fecha y hora (formato: dd/mm/yyyy hh:mm): ")
                try:
                    fecha_dt = datetime.strptime(fecha_hora_input, "%d/%m/%Y %H:%M")
                    break  # Sale del bucle si el formato es correcto
                except ValueError:
                    print("⚠️ Formato inválido. Intente nuevamente (ej: 10/05/2025 08:00).")

            # Registrar la medición
            mediciones.append({
                "parcela": parcela,
                "sensor": sensor,
                "valor": valor,
                "unidad": unidad,
                "fecha_hora": fecha_dt
            })

            print("✅ Medición registrada correctamente.")

    return mediciones
