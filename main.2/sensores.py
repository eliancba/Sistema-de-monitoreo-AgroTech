# sensores.py

def gestionar_sensores(sensores, sensores_en_parcelas, parcelas, num_sensor):
    """
    Submenú para gestionar los sensores.
    Permite agregar nuevos sensores, asignarlos a parcelas o eliminarlos.
    """
    opcion = ''
    while opcion != "6":
        print("\n---- GESTIÓN DE SENSORES ----")
        print("1. Ver Sensores Disponibles")
        print("2. Agregar Sensor")
        print("3. Ver Sensores Instalados")
        print("4. Instalar Sensor en Parcela")
        print("5. Eliminar Sensor de Parcela")
        print("6. Volver al Menú Principal")
        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            for s in sensores:
                print(f"Nro: {s['nro']} | Magnitud: {s['magnitud']} | Nombre: {s['nombre']} | Unidad: {s['unidad']}")

        elif opcion == "2":
            magnitud = input("Magnitud: ")
            nombre = input("Nombre técnico: ")
            unidad = input("Unidad de medida: ")
            sensores.append({"nro": num_sensor, "magnitud": magnitud, "nombre": nombre, "unidad": unidad})
            print(f"Sensor {num_sensor} agregado.")
            num_sensor += 1

        elif opcion == "3":
            if not sensores_en_parcelas:
                print("No hay sensores instalados.")
            else:
                for parcela, lista in sensores_en_parcelas.items():
                    print(f"Parcela {parcela}: Sensores instalados -> {lista}")

        elif opcion == "4":
            parcela = int(input("Número de parcela: "))
            sensor = int(input("Número de sensor: "))
            if any(p["nro"] == parcela for p in parcelas) and any(s["nro"] == sensor for s in sensores):
                sensores_en_parcelas.setdefault(parcela, []).append(sensor)
                print("Sensor instalado.")
            else:
                print("Parcela o sensor no encontrado.")

        elif opcion == "5":
            parcela = int(input("Número de parcela: "))
            sensor = int(input("Número de sensor: "))
            if parcela in sensores_en_parcelas and sensor in sensores_en_parcelas[parcela]:
                sensores_en_parcelas[parcela].remove(sensor)
                if not sensores_en_parcelas[parcela]:
                    del sensores_en_parcelas[parcela]
                print("Sensor eliminado.")
            else:
                print("Sensor no encontrado en la parcela.")

    return num_sensor
