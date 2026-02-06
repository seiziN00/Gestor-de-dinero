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

CREATE TABLE IF NOT EXISTS catalogo (
    categoria TEXT NOT NULL,
    id TEXT NOT NULL,
    nombre TEXT NOT NULL,
    disponible TEXT NOT NULL
);

INSERT INTO catalogo (categoria, id, nombre, disponible)
VALUES (1, 0, "TIPOS_MOVIMIENTO", 0),
       (1, 1, "ingreso", 1),
       (1, 2, "Gasto", 1),
       (1, 3, "Cambio", 1),
       (1, 4, "Préstamo", 1),
       (2, 0, "METODO_PAGO", 0),
       (2, 1, "Efectivo", 1),
       (2, 2, "Yape", 1),
       (2, 3, "Scotiabank/Plin", 1)