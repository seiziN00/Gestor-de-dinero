from config.constants import DEFAULTS

class TransferenciasState:
	"""docstring for TransferenciasState"""
	def __init__(self):
		self.tipo_movimiento = 1
		self.metodos_pago = set(DEFAULTS["metodos_pago"])