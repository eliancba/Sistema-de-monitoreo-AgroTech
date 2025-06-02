from db import conectar

# Registra una medición en la base de datos
def registrar_medicion(parcela_id, sensor_id, valor, unidad, fecha_hora):
    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO mediciones (parcela_id, sensor_id, valor, unidad, fecha_hora) VALUES (?, ?, ?, ?, ?)",
                (parcela_id, sensor_id, valor, unidad, fecha_hora))
    con.commit()
    con.close()

# Devuelve todas las mediciones ordenadas por fecha
def listar_mediciones():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT parcela_id, sensor_id, valor, unidad, fecha_hora FROM mediciones ORDER BY datetime(fecha_hora)")
    data = cur.fetchall()
    con.close()
    return data
