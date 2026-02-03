TIPOS_MOVIMIENTO = [
    {
        "id": 1,
        "label": "Ingreso",
        "selected": True
    },
    {
        "id": 2,
        "label": "Gasto",
        "selected": False
    },
    {
        "id": 3,
        "label": "Cambio",
        "selected": False
    },
    {
        "id": 4,
        "label": "Préstamo",
        "selected": False
    }
]

TIPOS_MOVIMIENTO_STATE = [t["id"] for t in TIPOS_MOVIMIENTO if t["selected"]]
TIPOS_MOVIMIENTO_BY_ID = {
    t["id"]: t["label"] for t in TIPOS_MOVIMIENTO
}


METODOS_PAGO = [
    {
        "id": 1,
        "label": "Efectivo",
        "default": True
    },
    {
        "id": 2,
        "label": "Yape",
        "default": False
    },
    {
        "id": 3,
        "label": "Scotiabank / Plin",
        "default": False
    }
]

METODO_PAGO_LABELS = [m["label"] for m in METODOS_PAGO]
METODO_PAGO_STATE = [m["label"] for m in METODOS_PAGO if m["default"]]