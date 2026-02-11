from db.database import get_connection
from db.movimientos_repo import (
    insertar_movimiento,
    insertar_metodo,
    insertar_nota,
    obtener_movimientos
)
from datetime import datetime

def registrar_transferencia(state, montos_por_metodo, nota):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        fecha = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        movimiento_id = insertar_movimiento(
            cursor,
            tipo_movimiento=state.tipo_movimiento,
            fecha=fecha
        )

        for metodo, monto in montos_por_metodo.items():
            insertar_metodo(cursor, movimiento_id, metodo, monto)

        if nota.strip():
            insertar_nota(cursor, movimiento_id, nota)

        obtener_movimientos(cursor)
        conn.commit()
        return movimiento_id

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()

# Tener cuidado con fecha, yo pensaba guardar solo dd-mm-aaaa, pero para si voy a interactuar con una base de datos entonces debo considerar hh:mm:ss para que al mostrar los datos en el Treeview se vean en orden preciso tal cual como fueron añadidos. La librería exacta es datetime.datetime, usar datetime.now().strftime("%d-%m-%Y %H:%M:%S")