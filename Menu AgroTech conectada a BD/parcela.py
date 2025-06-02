from db import conectar  # Importa conexión a base de datos

# Agrega una nueva parcela a la base de datos
def agregar_parcela(ubicacion, size, cultivo):
    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO parcelas (ubicacion, size, cultivo) VALUES (?, ?, ?)", (ubicacion, size, cultivo))
    con.commit()
    con.close()

# Lista todas las parcelas almacenadas
def listar_parcelas():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT * FROM parcelas")
    parcelas = cur.fetchall()  # Devuelve una lista de tuplas
    con.close()
    return parcelas

# Modifica una parcela existente por ID
def modificar_parcela(nro, ubicacion, size, cultivo):
    con = conectar()
    cur = con.cursor()
    cur.execute("UPDATE parcelas SET ubicacion=?, size=?, cultivo=? WHERE nro=?", (ubicacion, size, cultivo, nro))
    con.commit()
    con.close()

# Elimina una parcela y sus asociaciones con sensores
def eliminar_parcela(nro):
    con = conectar()
    cur = con.cursor()
    cur.execute("DELETE FROM sensores_en_parcelas WHERE parcela_id=?", (nro,))
    cur.execute("DELETE FROM parcelas WHERE nro=?", (nro,))
    con.commit()
    con.close()
