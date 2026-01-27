def hacer_cambio(datos):
	if datos["origen"] == datos["destino"]:
		raise ValueError("No puedes cambiar al mismo método")

	if datos["monto"] <= 0:
		raise ValueError("Monto inválido")

	# Más lógica...