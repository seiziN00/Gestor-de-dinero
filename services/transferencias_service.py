from db.database import get_connection
from db.movimientos_repo import (
    insertar_movimiento,
    insertar_metodo,
    insertar_nota
)
from datetime import date

def registrar_transferencia(state, montos_por_metodo, nota):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        fecha = date.today().strftime("%d-%m-%Y")

        movimiento_id = insertar_movimiento(
            cursor,
            tipo_movimiento=state.tipo_movimiento,
            fecha=fecha
        )

        for metodo, monto in montos_por_metodo.items():
            insertar_metodo(cursor, movimiento_id, metodo, monto)

        if nota:
            insertar_nota(cursor, movimiento_id, nota)

        conn.commit()
        return movimiento_id

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()
