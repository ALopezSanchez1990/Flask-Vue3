import sqlite3
DATABASE_NAME = "articles.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    print("Base de datos abierta en articles correctamente")
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS category(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(256) NOT NULL
            )
        """,
        """CREATE TABLE IF NOT EXISTS article(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo VARCHAR(256) NOT NULL,
				cuerpo TEXT NOT NULL,
                fechaPublicacion Date NOT NULL,
                etiqueta VARCHAR(32),
                categoria INTEGER NOT NULL,
                FOREIGN KEY(categoria) REFERENCES category(id)
            )
        """
    ]
    db = get_db()
    cursor = db.cursor()
    db.execute('PRAGMA foreign_keys = ON')
    for table in tables:
        cursor.execute(table)