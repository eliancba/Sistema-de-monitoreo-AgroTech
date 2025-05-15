# consultas.py

def gestionar_consultas(mediciones, parcelas, sensores, sensores_en_parcelas):
    """
    Submenú de consultas para visualizar datos de mediciones.
    """
    while True:
        print("\n---- CONSULTAS ----")
        print("1. Ver mediciones por parcela")
        print("2. Ver mediciones por sensor")
        print("3. Ver promedio por tipo de sensor")
        print("4. Filtrar mediciones por fechas")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nro = int(input("Ingrese número de parcela: "))
            print(f"\nMediciones para la parcela {nro}:")
            for m in mediciones:
                if m["parcela"] == nro:
                    sensor = next((s for s in sensores if s["nro"] == m["sensor"]), None)
                    if sensor:
                        print(f"- {m['fecha_hora']} | {sensor['magnitud']}: {m['valor']} {m['unidad']}")

        elif opcion == "2":
            nro = int(input("Ingrese número de sensor: "))
            print(f"\nMediciones para el sensor {nro}:")
            for m in mediciones:
                if m["sensor"] == nro:
                    parcela = next((p for p in parcelas if p["nro"] == m["parcela"]), None)
                    if parcela:
                        print(f"- {m['fecha_hora']} | Parcela {parcela['nro']} ({parcela['cultivo']}): {m['valor']} {m['unidad']}")

        elif opcion == "3":
            print("\nPromedio por tipo de sensor:")
            for sensor in sensores:
                valores = [float(m["valor"]) for m in mediciones if m["sensor"] == sensor["nro"]]
                if valores:
                    promedio = sum(valores) / len(valores)
                    print(f"- {sensor['magnitud']}: {promedio:.2f} {sensor['unidad']}")
                else:
                    print(f"- {sensor['magnitud']}: sin datos")

        elif opcion == "4":
            inicio_str = input("Fecha de inicio (dd/mm/yyyy): ")
            fin_str = input("Fecha de fin (dd/mm/yyyy): ")
            try:
                inicio = datetime.strptime(inicio_str, "%d/%m/%Y")
                fin = datetime.strptime(fin_str, "%d/%m/%Y")
                print(f"\nMediciones entre {inicio_str} y {fin_str}:")
                for m in mediciones:
                    if inicio <= m["fecha_hora"] <= fin:
                        sensor = next((s for s in sensores if s["nro"] == m["sensor"]), None)
                        print(f"- {m['fecha_hora']} | Parcela {m['parcela']} | {sensor['magnitud']}: {m['valor']} {m['unidad']}")
            except ValueError:
                print("⚠️ Formato de fecha inválido. Use dd/mm/yyyy.")

        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
