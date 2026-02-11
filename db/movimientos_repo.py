# Transferencias: Contiene el SQL relacionado con las transacciones
def insertar_movimiento(cursor, tipo_movimiento, fecha):
    cursor.execute("""
        INSERT INTO movimientos (tipo_movimiento, fecha)
        VALUES (?, ?)
    """, (tipo_movimiento, fecha))

    return cursor.lastrowid

def insertar_metodo(cursor, movimiento_id, metodo_pago, monto):
    cursor.execute("""
        INSERT INTO movimiento_metodos (movimiento_id, metodo_pago, monto)
        VALUES (?, ?, ?)
    """, (movimiento_id, metodo_pago, monto))

def insertar_nota(cursor, movimiento_id, nota):
    cursor.execute("""
        INSERT INTO notas (movimiento_id, nota)
        VALUES (?, ?)   
    """, (movimiento_id, nota))

def obtener_movimientos(cursor):
    cursor.execute("""
        SELECT 
            m.tipo_movimiento,
            mm.metodo_pago,
            mm.monto
        FROM movimientos m
        JOIN movimiento_metodos mm 
            ON m.id = mm.movimiento_id
        ORDER BY m.fecha DESC
        LIMIT 10
    """)
    return cursor.fetchall()

# Lógica para Dashboard
def mostrar_ultimos_cinco_movimientos(cursor):
    cursor.execute("""
        SELECT 
            m.tipo_movimiento,
            mm.metodo_pago,
            mm.monto,
            m.fecha
        FROM movimientos m
        JOIN movimiento_metodos mm 
            ON m.id = mm.movimiento_id
        ORDER BY m.fecha DESC
        LIMIT 5
    """)
    return cursor.fetchall()