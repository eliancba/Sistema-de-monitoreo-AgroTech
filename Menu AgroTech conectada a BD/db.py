import sqlite3  # Librería estándar para trabajar con bases de datos SQLite

# Función que retorna una conexión a la base de datos agrotech.db
def conectar():
    return sqlite3.connect("agrotech.db")

# Crea las tablas necesarias si no existen aún
def inicializar_db():
    con = conectar()             # Abre conexión
    cur = con.cursor()           # Crea cursor para ejecutar comandos SQL

    # Tabla de parcelas agrícolas
    cur.execute("""
        CREATE TABLE IF NOT EXISTS parcelas (
            nro INTEGER PRIMARY KEY AUTOINCREMENT,  -- ID autoincremental
            ubicacion TEXT,                         -- Coordenadas de ubicación
            size TEXT,                              -- Tamaño en hectáreas
            cultivo TEXT                            -- Tipo de cultivo
        )
    """)

    # Tabla de sensores
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sensores (
            nro INTEGER PRIMARY KEY AUTOINCREMENT,  -- ID sensor
            magnitud TEXT,                          -- Qué mide
            nombre TEXT,                            -- Nombre técnico
            unidad TEXT                             -- Unidad de medida
        )
    """)

    # Asociación de sensores con parcelas
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sensores_en_parcelas (
            parcela_id INTEGER,                     -- ID parcela
            sensor_id INTEGER,                      -- ID sensor
            PRIMARY KEY(parcela_id, sensor_id)      -- Clave compuesta
        )
    """)

    # Mediciones realizadas por sensores
    cur.execute("""
        CREATE TABLE IF NOT EXISTS mediciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,   -- ID de la medición
            parcela_id INTEGER,                     -- ID parcela medida
            sensor_id INTEGER,                      -- ID sensor usado
            valor TEXT,                             -- Valor medido
            unidad TEXT,                            -- Unidad
            fecha_hora TEXT                         -- Fecha y hora de medición
        )
    """)

    con.commit()  # Guarda los cambios
    con.close()   # Cierra conexión
