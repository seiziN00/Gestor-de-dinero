DEFAULTS = {
    "tipo_movimiento": 1,
    "metodos_pago": ["Efectivo"]
}

TIPOS_MOVIMIENTO = {
    1: "Ingreso",
    2: "Gasto",
    3: "Cambio",
    4: "Préstamo"
}

METODOS_PAGO = [
    {
        "id": "efectivo",
        "label": "Efectivo",
        "default": True
    },
    {
        "id": "yape",
        "label": "Yape",
        "default": False
    },
    {
        "id": "plin",
        "label": "Scotiabank / Plin",
        "default": False
    }
]

METODO_PAGO_LABELS = [m["label"] for m in METODOS_PAGO]

METODO_PAGO_BY_LABEL = {
    m["label"]: m["id"] for m in METODOS_PAGO
}

METODO_PAGO_BY_ID = {
    m["id"]: m["label"] for m in METODOS_PAGO
}