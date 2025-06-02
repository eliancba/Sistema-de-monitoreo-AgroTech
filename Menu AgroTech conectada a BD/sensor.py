from db import conectar

# Agrega un nuevo sensor a la base de datos
def agregar_sensor(magnitud, nombre, unidad):
    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO sensores (magnitud, nombre, unidad) VALUES (?, ?, ?)", (magnitud, nombre, unidad))
    con.commit()
    con.close()

# Lista todos los sensores disponibles
def listar_sensores():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT * FROM sensores")
    sensores = cur.fetchall()
    con.close()
    return sensores

# Asocia un sensor a una parcela (instalación)
def instalar_sensor(parcela_id, sensor_id):
    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT OR IGNORE INTO sensores_en_parcelas (parcela_id, sensor_id) VALUES (?, ?)", (parcela_id, sensor_id))
    con.commit()
    con.close()

# Elimina una asociación sensor-parcela
def eliminar_sensor_de_parcela(parcela_id, sensor_id):
    con = conectar()
    cur = con.cursor()
    cur.execute("DELETE FROM sensores_en_parcelas WHERE parcela_id=? AND sensor_id=?", (parcela_id, sensor_id))
    con.commit()
    con.close()

# Lista todas las asociaciones actuales de sensores en parcelas
def sensores_instalados():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT * FROM sensores_en_parcelas")
    data = cur.fetchall()
    con.close()
    return data
