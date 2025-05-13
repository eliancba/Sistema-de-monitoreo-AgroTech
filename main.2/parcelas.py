# parcelas.py

def gestionar_parcelas(parcelas, sensores_en_parcelas, num_parcela):
    """
    Submenú para gestionar las parcelas agrícolas.
    Permite visualizar, agregar, modificar o eliminar parcelas.
    """
    opcion = ''
    while opcion != "5":
        print("\n---- GESTIÓN DE PARCELAS ----")
        print("1. Ver Registro de Parcelas")
        print("2. Agregar Parcela")
        print("3. Modificar Parcela")
        print("4. Eliminar Parcela")
        print("5. Volver al Menú Principal")
        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            print("Parcelas registradas:")
            if not parcelas:
                print("No hay parcelas registradas.")
            else:
                for p in parcelas:
                    print(f"Nro: {p['nro']} | Ubicación: {p['ubicacion']} | Tamaño: {p['size']} ha | Cultivo: {p['cultivo']}")

        elif opcion == "2":
            ubicacion = input("Ubicación (lat, long): ")
            size = input("Tamaño en hectáreas: ")
            cultivo = input("Tipo de cultivo: ")
            nueva = {"nro": num_parcela, "ubicacion": ubicacion, "size": size, "cultivo": cultivo}
            parcelas.append(nueva)
            print(f"Parcela {num_parcela} agregada.")
            num_parcela += 1

        elif opcion == "3":
            nro = int(input("Número de parcela a modificar: "))
            encontrada = False
            for p in parcelas:
                if p["nro"] == nro:
                    print(f"Parcela actual: {p}")
                    p["ubicacion"] = input("Nueva ubicación: ")
                    p["size"] = input("Nuevo tamaño: ")
                    p["cultivo"] = input("Nuevo cultivo: ")
                    print("Parcela modificada.")
                    encontrada = True
                    break
            if not encontrada:
                print("Parcela no encontrada.")

        elif opcion == "4":
            nro = int(input("Número de parcela a eliminar: "))
            confirm = input("¿Está seguro? (s/n): ")
            if confirm.lower() == 's':
                for p in parcelas:
                    if p["nro"] == nro:
                        parcelas.remove(p)
                        sensores_en_parcelas.pop(nro, None)
                        print("Parcela eliminada.")
                        break
                else:
                    print("Parcela no encontrada.")

    return num_parcela
