from db.database import get_connection
from db.movimientos_repo import mostrar_ultimos_cinco_movimientos

def listar_movimientos():
	with get_connection() as conn:
		cursor = conn.cursor()
		return mostrar_ultimos_cinco_movimientos(cursor)