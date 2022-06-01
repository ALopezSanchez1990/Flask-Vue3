from db.db import get_db

def get_all_articles():
    db = get_db()
    cursor = db.cursor()
    query = "Select * from article"
    cursor.execute(query)
    return cursor.fetchall()

def get_article_by_id(id: int):
    db = get_db()
    cursor = db.cursor()
    query = "Select * from article where id = ?"
    cursor.execute(query, [id])
    return cursor.fetchone()

def create_article(article):
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO article(titulo, cuerpo, fechaPublicacion, categoria, etiqueta) VALUES (?, ?, ?, ? , ?)"
    # falta article.id,...
    cursor.execute(query, [])
    db.commit()
    return True

def update_article(article):
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO article(titulo, cuerpo, fechaPublicacion, categoria, etiqueta) VALUES (?, ?, ?, ? , ?)"
    # mirar updates
    cursor.execute(query, [])
    db.commit()
    return True

def delete_article(id: int):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE * FROM article where id = ?"
    # mirar deletes
    cursor.execute(query, [id])
    db.commit()
    return True