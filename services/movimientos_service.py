from db.database import get_connection
from db.movimientos_repo import obtener_movimientos
#from config.constants import METODOS_PAGO, TIPOS_MOVIMIENTO

def listar_movimientos():
	with get_connection() as conn:
		cursor = conn.cursor()
		return obtener_movimientos(cursor)