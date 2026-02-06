from db.database import get_connection

def init_db():
	connection = get_connection()
	with open("db/schema.sql", "r", encoding="utf-8") as f:
		connection.executescript(f.read())
	connection.commit()
	connection.close()