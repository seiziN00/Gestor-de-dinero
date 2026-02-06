# Conexión a la base de datos SQLite
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "gestor_dinero.db"

def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection