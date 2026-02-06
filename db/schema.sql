CREATE TABLE IF NOT EXISTS movimientos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo_movimiento INTEGER NOT NULL,
    fecha TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS movimiento_metodos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    movimiento_id INTEGER NOT NULL,
    metodo_pago INTEGER NOT NULL,
    monto REAL NOT NULL,
    FOREIGN KEY (movimiento_id) REFERENCES movimientos(id)
);

CREATE TABLE IF NOT EXISTS notas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    movimiento_id INTEGER NOT NULL,
    texto TEXT,
    FOREIGN KEY (movimiento_id) REFERENCES movimientos(id)
);

CREATE TABLE IF NOT EXISTS cambios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    movimiento_id INTEGER NOT NULL,
    monto REAL NOT NULL,
    origen INTEGER NOT NULL,
    destino INTEGER NOT NULL,
    FOREIGN KEY (movimiento_id) REFERENCES movimientos(id)
);