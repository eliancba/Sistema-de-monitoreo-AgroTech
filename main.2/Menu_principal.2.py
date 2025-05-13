# menu_principal.py

# --------------------------
# DATOS GLOBALES DEL SISTEMA
# --------------------------

# Lista de parcelas registradas
parcelas = [
    {"nro": 1, "ubicacion": "Lat: -34.60, Long: -58.38", "size": "12", "cultivo": "Soja"},
    {"nro": 2, "ubicacion": "Lat: -31.42, Long: -64.18", "size": "20", "cultivo": "Maíz"}
]

# Lista de sensores disponibles
sensores = [
    {"nro": 1, "magnitud": "Humedad del suelo", "nombre": "Capacitive Soil Moisture Sensor v1.2 / v2.0", "unidad": "%"},
    {"nro": 2, "magnitud": "Temperatura del ambiente", "nombre": "DS18B20", "unidad": "°C"}
]

# Diccionario con sensores instalados por parcela (clave = nro parcela, valor = lista de sensores)
sensores_en_parcelas = {}

# Lista de mediciones registradas
mediciones = []

# Contadores para nuevas entidades
num_parcela = 3
num_sensor = 3

# -------------------------------------
# IMPORTACIÓN DE LOS SUBMENÚS MODULARES
# -------------------------------------

from parcelas import gestionar_parcelas
from sensores import gestionar_sensores
from mediciones import gestionar_mediciones
from consultas import gestionar_consultas

# --------------------------
# MENÚ PRINCIPAL DEL SISTEMA
# --------------------------

print("Bienvenidos al sistema de Monitoreo de AgroTech Coop")

opcion = ''
while opcion != "5":
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Gestionar Parcelas")
    print("2. Gestionar Sensores")
    print("3. Gestionar Mediciones")
    print("4. Consultar Datos")
    print("5. Salir")

    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        # Invoca el submenú de parcelas
        num_parcela = gestionar_parcelas(parcelas, sensores_en_parcelas, num_parcela)

    elif opcion == "2":
        # Invoca el submenú de sensores
        num_sensor = gestionar_sensores(sensores, sensores_en_parcelas, parcelas, num_sensor)

    elif opcion == "3":
        # Invoca el submenú de mediciones
        mediciones = gestionar_mediciones(mediciones, parcelas, sensores, sensores_en_parcelas)

    elif opcion == "4":
        # Invoca el submenú de consultas
        gestionar_consultas(mediciones, parcelas, sensores, sensores_en_parcelas)

    elif opcion != "5":
        print("Opción no válida. Intente nuevamente.")
