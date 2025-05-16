from datetime import datetime  # Importa el módulo datetime para trabajar con fechas y horas

# --------------------------
# DATOS GLOBALES DEL SISTEMA
# --------------------------

# Lista de parcelas registradas en el sistema, cada una con su número, ubicación, tamaño y tipo de cultivo. Se pueden agregar mas a lo largo de la ejecucion del programa.
parcelas = [
    {"nro": 1, "ubicacion": "Lat: -34.60, Long: -58.38", "size": "12", "cultivo": "Soja"},
    {"nro": 2, "ubicacion": "Lat: -31.42, Long: -64.18", "size": "20", "cultivo": "Maíz"}
]

# Lista de sensores disponibles, con su número, tipo de magnitud que mide, nombre técnico y unidad de medida. Se pueden agregar mas a lo largo de la ejecucion del programa.
sensores = [
    {"nro": 1, "magnitud": "Humedad del suelo", "nombre": "Capacitive Soil Moisture Sensor v1.2 / v2.0", "unidad": "%"},
    {"nro": 2, "magnitud": "Temperatura del ambiente", "nombre": "DS18B20", "unidad": "°C"}
]

# Diccionario que asocia parcelas con listas de sensores instalados en ellas
sensores_en_parcelas = {}

# Lista para almacenar las mediciones registradas (parcela, sensor, valor, unidad, fecha/hora)
mediciones = []

# Contadores para asignar números a nuevas parcelas y sensores
num_parcela = 3
num_sensor = 3

# --------------------------
# MENÚ PRINCIPAL DEL SISTEMA
# --------------------------

print("Bienvenidos al sistema de Monitoreo de AgroTech Coop")

opcion = ""
# Bucle principal que muestra el menú hasta que el usuario elige salir
while opcion != "5":
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Gestionar Parcelas")
    print("2. Gestionar Sensores")
    print("3. Registrar Mediciones")
    print("4. Consultar Datos")
    print("5. Salir")
    opcion = input("Ingrese su opción: ")

    # Gestión de Parcelas
    if opcion == "1":
        subop = ""
        while subop != "5":
            print("\n---- GESTIÓN DE PARCELAS ----")
            print("1. Ver Parcelas")
            print("2. Agregar Parcela")
            print("3. Modificar Parcela")
            print("4. Eliminar Parcela")
            print("5. Volver al Menú Principal")
            subop = input("Ingrese su opción: ")

            # Visualización de parcelas existentes
            if subop == "1":
                print("Eligió ver parcelas")
                if not parcelas:
                    print("No hay parcelas registradas.")
                else:
                    for p in parcelas:
                        print(f"Nro: {p['nro']} | Ubicación: {p['ubicacion']} | Tamaño: {p['size']} ha | Cultivo: {p['cultivo']}")
            
            # Agregar nueva parcela
            elif subop == "2":
                print("Eligió agregar parcela")
                ubicacion = input("Ubicación (lat, long): ")
                size = input("Tamaño en hectáreas: ")
                cultivo = input("Tipo de cultivo: ")
                parcelas.append({"nro": num_parcela, "ubicacion": ubicacion, "size": size, "cultivo": cultivo})
                print("Se guardó la parcela")
                num_parcela += 1  # Incrementa el contador de parcelas

            # Modificar datos de una parcela existente
            elif subop == "3":
                nro = int(input("Número de parcela a modificar: "))
                for p in parcelas:
                    if p["nro"] == nro:
                        p["ubicacion"] = input("Nueva ubicación: ")
                        p["size"] = input("Nuevo tamaño: ")
                        p["cultivo"] = input("Nuevo cultivo: ")
                        print("Parcela modificada")
                        break
                else:
                    print("Parcela no encontrada")

            # Eliminar una parcela del sistema (también quita sensores asociados)
            elif subop == "4":
                nro = int(input("Número de parcela a eliminar: "))
                confirm = input("¿Está seguro? (s/n): ")
                if confirm.lower() == "s":
                    for p in parcelas:
                        if p["nro"] == nro:
                            parcelas.remove(p)
                            sensores_en_parcelas.pop(nro, None)  # Elimina sensores asociados si existen
                            print("Parcela eliminada")
                            break
                    else:
                        print("Parcela no encontrada")

    # Gestión de Sensores
    elif opcion == "2":
        subop = ""
        while subop != "6":
            print("\n---- GESTIÓN DE SENSORES ----")
            print("1. Ver Sensores Disponibles")
            print("2. Agregar Sensor")
            print("3. Ver Sensores Instalados")
            print("4. Instalar Sensor en Parcela")
            print("5. Eliminar Sensor de Parcela")
            print("6. Volver al Menú Principal")
            subop = input("Ingrese su opción: ")

            # Muestra la lista de sensores disponibles
            if subop == "1":
                for s in sensores:
                    print(f"Nro: {s['nro']} | Magnitud: {s['magnitud']} | Nombre: {s['nombre']} | Unidad: {s['unidad']}")
            
            # Agrega un nuevo sensor al sistema
            elif subop == "2":
                magnitud = input("Magnitud: ")
                nombre = input("Nombre técnico: ")
                unidad = input("Unidad de medida: ")
                sensores.append({"nro": num_sensor, "magnitud": magnitud, "nombre": nombre, "unidad": unidad})
                print("Sensor agregado")
                num_sensor += 1  # Incrementa el contador de sensores

            # Muestra los sensores actualmente instalados en cada parcela
            elif subop == "3":
                if not sensores_en_parcelas:
                    print("No hay sensores instalados")
                else:
                    for parcela, lista in sensores_en_parcelas.items():
                        print(f"Parcela {parcela}: Sensores instalados -> {lista}")

            # Asocia un sensor a una parcela específica
            elif subop == "4":
                parcela = int(input("Número de parcela: "))
                sensor = int(input("Número de sensor: "))
                if any(p["nro"] == parcela for p in parcelas) and any(s["nro"] == sensor for s in sensores):
                    sensores_en_parcelas.setdefault(parcela, []).append(sensor)
                    print("Sensor instalado")
                else:
                    print("Parcela o sensor no encontrado")

            # Elimina la asociación de un sensor con una parcela
            elif subop == "5":
                parcela = int(input("Número de parcela: "))
                sensor = int(input("Número de sensor: "))
                if parcela in sensores_en_parcelas and sensor in sensores_en_parcelas[parcela]:
                    sensores_en_parcelas[parcela].remove(sensor)
                    if not sensores_en_parcelas[parcela]:  # Elimina la clave si no quedan sensores
                        del sensores_en_parcelas[parcela]
                    print("Sensor eliminado")
                else:
                    print("Sensor no encontrado en la parcela")

    # Registro de mediciones realizadas por sensores
    elif opcion == "3":
        print("\n---- REGISTRO DE MEDICIONES ----")
        parcela = int(input("Ingrese número de parcela: "))
        if parcela not in sensores_en_parcelas or not sensores_en_parcelas[parcela]:
            print("La parcela no tiene sensores instalados.")
        else:
            print(f"Sensores instalados en Parcela {parcela}: {sensores_en_parcelas[parcela]}")
            sensor = int(input("Ingrese número de sensor: "))
            if sensor in sensores_en_parcelas[parcela]:
                valor = input("Ingrese valor: ")
                unidad = input("Ingrese unidad: ")
                # Solicita una fecha válida en el formato correcto
                while True:
                    fecha = input("Ingrese fecha y hora (dd/mm/yyyy hh:mm): ")
                    try:
                        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y %H:%M")
                        break
                    except ValueError:
                        print("Formato inválido. Intente nuevamente.")
                # Registra la medición en la lista global
                mediciones.append({
                    "parcela": parcela,
                    "sensor": sensor,
                    "valor": valor,
                    "unidad": unidad,
                    "fecha_hora": fecha_dt
                })
                print("Medición registrada correctamente.")
            else:
                print("Sensor no instalado en esa parcela.")

    # Consulta de mediciones registradas
    elif opcion == "4":
        print("\n---- CONSULTAS ----")
        print("Mediciones registradas:")
        if not mediciones:
            print("No hay mediciones registradas.")
        else:
            # Ordena las mediciones por fecha y las muestra
            for m in sorted(mediciones, key=lambda x: x["fecha_hora"]):
                print(f"Parcela {m['parcela']} - Sensor {m['sensor']} - {m['valor']} {m['unidad']} - {m['fecha_hora'].strftime('%d/%m/%Y %H:%M')}")

    # Salida del programa
    elif opcion == "5":
        print("Eligió salir. ¡Hasta luego!")
    else:
        print("Opción no válida. Intente nuevamente.")