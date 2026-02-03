from config.constants import TIPOS_MOVIMIENTO_STATE, METODO_PAGO_STATE

class TransferenciasState:
	def __init__(self):
		self.tipo_movimiento: int = (
			TIPOS_MOVIMIENTO_STATE[0] if TIPOS_MOVIMIENTO_STATE else 1
		)
		self.metodos_pago: set[int] = set(METODO_PAGO_STATE)