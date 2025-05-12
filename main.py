""" Estructura de menu para Cooperativa agro.

"""

parcelas = [
     {
        "nro": 1,
        "ubicacion": "Lat: -34.60, Long: -58.38",
        "size": "12",
        "cultivo": "Soja"
    },
    {
        "nro": 2,
        "ubicacion": "Lat: -31.42, Long: -64.18",
        "size": "20",
        "cultivo": "Maíz"
    }
]
num_parcela = 3


print ("Bienvenidos al sistema de Monitoreo de AgroTech Coop")
opcion = ''

while opcion != "5":
    print ("MENU PRINCIPAL")
    print ("1. Gestionar Parcelas")
    print ("2. Gestionar Sensores")
    print ("3. Gestionar Mediciones")
    print ("4. Consultar Datos")
    print ("5. Salir")

    opcion = input ("Ingrese seleccion: ")

    if opcion == "1":
        print ("----Gestion de Parcelas----")
        print("1. Ver Registro de Parcelas")
        print("2. Agregar Parcela")
        print("3. Modificar Parcela")
        print("4. Eliminar Parcela")
        print("5. Volver al Menu Principal")
        opcion_sec = input ("Ingese seleccion: ")

        if opcion_sec == "1":
            print("Parcelas Registradas: ")
            if len(parcelas) == 0:
                print("No hay Registro")
            else:
                for p in parcelas:
                    print(f"Nro: {p['nro']} | Ubicacion: {p['ubicacion']} | Tamaño: {p['size']} | Cultivo: {p['cultivo']}")
        elif opcion_sec == "2":
            print("Agregar Parcela:")
            ubicacion = input("Ingrese (latitud, longitud): ")
            size = input("Ingrese Tamaño(hectareas): ")
            cultivo = input("Ingrese tipo de cultivo: ")

            parcela = {
                "nro": num_parcela,
                "ubicacion": ubicacion,
                "size": size,
                "cultivo": cultivo
            }

            parcelas.append(parcela)
            print(f"Parcela {num_parcela} agregada con éxito.")
            num_parcela += 1
        elif opcion_sec == "3":
            print("Modificar Parcela")
            numero = int(input ("Ingrese el Numero de Parcela a modificar: "))
            encontrada = False
            for p in parcelas: 
                if p["nro"] == numero:
                    print(f"Parcela Seleccionada: Ubicacion: {p['ubicacion']}, Tamaño: {p['size']}, Cultivo: {p['cultivo']}")
                    p["ubicacion"] = input("Nueva Ubicacion: ")
                    p["size"] = input("Nuevo tamaño: ")
                    p["cultivo"] = input("Nuevo tipo de Cultivo: ")
                    print("Parcela Modificada.")
                    encontrada = True
                    break
                if not encontrada:
                    print("Parcela no encontrada.")
        elif opcion_sec == "4":
            print("Eliminar Parcela")
            numero = int(input("Ingrese el Numero de Parcela: "))
            confirmacion = input("¿Estas Seguro? (s/n)")
            if confirmacion.lower() == 's':
                eliminada = False
                for p in parcelas:
                    if p["nro"] == numero:
                        parcelas.remove(p)
                        print("Parcela eliminada")
                        eliminada = True
                        break
                if not eliminada:
                    print("Parcela no encontrada.")
                else: 
                    print("Eliminacion Cancelada.")
        elif opcion_sec == "5":
            print("Volviendo al menu")



    elif opcion == "2":
        print ("Gestion de Sensores")
        print("en proceso...")
        opcion_sec = input ("Ingese seleccion: ")
    
    elif opcion == "3":
        print ("Gestion de Mediciones")
        print("en proceso...")
        opcion_sec = input ("Ingese seleccion: ")

    elif opcion == "4":
        print ("Consulta Base de Datos")
        print("en proceso...")
        opcion_sec = input ("Ingese seleccion: ")

    elif opcion =="5":
        print("Saliendo..")
    else:
        print ("Opcion incorrecta.")
