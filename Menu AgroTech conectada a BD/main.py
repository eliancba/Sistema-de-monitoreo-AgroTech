from datetime import datetime
from db import inicializar_db
from parcela import agregar_parcela, listar_parcelas, modificar_parcela, eliminar_parcela
from sensor import agregar_sensor, listar_sensores, instalar_sensor, eliminar_sensor_de_parcela, sensores_instalados
from medicion import registrar_medicion, listar_mediciones

# Inicializa la base de datos (crea las tablas si no existen)
inicializar_db()

print("Bienvenidos al sistema de Monitoreo de AgroTech Coop")

opcion = ""
while opcion != "5":
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Gestionar Parcelas")
    print("2. Gestionar Sensores")
    print("3. Registrar Mediciones")
    print("4. Consultar Datos")
    print("5. Salir")
    opcion = input("Ingrese su opción: ")

    # Submenú Parcelas
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

            if subop == "1":
                for p in listar_parcelas():
                    print(f"Nro: {p[0]} | Ubicación: {p[1]} | Tamaño: {p[2]} ha | Cultivo: {p[3]}")
            elif subop == "2":
                agregar_parcela(input("Ubicación: "), input("Tamaño: "), input("Cultivo: "))
            elif subop == "3":
                modificar_parcela(int(input("Nro parcela: ")), input("Ubicación: "), input("Tamaño: "), input("Cultivo: "))
            elif subop == "4":
                eliminar_parcela(int(input("Nro parcela: ")))

    # Submenú Sensores
    elif opcion == "2":
        subop = ""
        while subop != "6":
            print("\n---- GESTIÓN DE SENSORES ----")
            print("1. Ver Sensores")
            print("2. Agregar Sensor")
            print("3. Ver Sensores Instalados")
            print("4. Instalar Sensor en Parcela")
            print("5. Eliminar Sensor de Parcela")
            print("6. Volver")
            subop = input("Ingrese su opción: ")

            if subop == "1":
                for s in listar_sensores():
                    print(f"Nro: {s[0]} | Magnitud: {s[1]} | Nombre: {s[2]} | Unidad: {s[3]}")
            elif subop == "2":
                agregar_sensor(input("Magnitud: "), input("Nombre técnico: "), input("Unidad: "))
            elif subop == "3":
                for item in sensores_instalados():
                    print(f"Parcela: {item[0]} -> Sensor: {item[1]}")
            elif subop == "4":
                instalar_sensor(int(input("Nro parcela: ")), int(input("Nro sensor: ")))
            elif subop == "5":
                eliminar_sensor_de_parcela(int(input("Nro parcela: ")), int(input("Nro sensor: ")))

    # Registro de mediciones
    elif opcion == "3":
        parcela = int(input("Parcela ID: "))
        sensor = int(input("Sensor ID: "))
        valor = input("Valor: ")
        unidad = input("Unidad: ")
        while True:
            fecha = input("Fecha y hora (dd/mm/yyyy hh:mm): ")
            try:
                fecha_dt = datetime.strptime(fecha, "%d/%m/%Y %H:%M")
                break
            except ValueError:
                print("Formato inválido")
        registrar_medicion(parcela, sensor, valor, unidad, fecha_dt.strftime("%Y-%m-%d %H:%M:%S"))

    # Consultar datos registrados
    elif opcion == "4":
        for m in listar_mediciones():
            print(f"Parcela {m[0]} - Sensor {m[1]} - {m[2]} {m[3]} - {m[4]}")

    elif opcion == "5":
        print("¡Hasta luego!")
