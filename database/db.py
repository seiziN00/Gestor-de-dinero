import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "gestor_dinero.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cuentas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        tipo TEXT NOT NULL,
        saldo REAL NOT NULL DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()
