import sqlite3

DB_NAME = "ropastore.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS prendas (
            codigo TEXT PRIMARY KEY,
            nombre TEXT,
            talla TEXT,
            stock INTEGER,
            precio TEXT
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS ventas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT,
            fecha TEXT
        )
    """)
    conn.commit()
    conn.close()

def get_prenda(codigo):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM prendas WHERE codigo = ?", (codigo,))
    result = c.fetchone()
    conn.close()
    return result

def registrar_venta(codigo):
    from datetime import datetime
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    prenda = get_prenda(codigo)
    if prenda and prenda[3] > 0:
        c.execute("UPDATE prendas SET stock = stock - 1 WHERE codigo = ?", (codigo,))
        c.execute("INSERT INTO ventas (codigo, fecha) VALUES (?, ?)", (codigo, datetime.now().isoformat()))
        conn.commit()
        conn.close()
        return True, prenda[1]
    conn.close()
    return False, None
