from db.db import get_db

def get_all_categories():
    db = get_db()
    cursor = db.cursor()
    query = "Select id, title from category"
    cursor.execute(query)
    return cursor.fetchall()

def create_article():
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO article(titulo, cuerpo, fechaPublicacion, categoria, etiqueta) VALUES (?, ?, ?, ? , ?)"
    cursor.execute(query, [])
    return cursor.fetchall()