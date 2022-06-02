from sqlite3 import Date
from db.db import get_db

def get_all_articles():
    try:
        db = get_db()
        cursor = db.cursor()
        query = "Select * from article"
        articles = cursor.execute(query).fetchall()
        results = {
            'articles': []
        }

        [results['articles'].append(parse_row(article)) for article in articles]

        db.close()
        return results
    except Exception as e:
        print(e)
        return { 'created': False }
    finally:
        db.close()

def get_article_by_id(id: int):
    db = get_db()
    cursor = db.cursor()
    query = "Select * from article where id = ?"
    fetched  = cursor.execute(query, [id]).fetchone()
    result = parse_row(fetched)
    return result

def create_article(article):
    try:
        db = get_db()
        cursor = db.cursor()
        query = "INSERT INTO article(titulo, cuerpo, fechaPublicacion, categoria, etiqueta) VALUES (?, ?, ?, ? , ?)"
        # falta article.id,...
        now = Date.today()
        cursor.execute(query, [article['titulo'], article['cuerpo'], now, article['categoria'], article['etiqueta']])
        db.commit()
        return { 'created': True }
    except Exception as e:
        print(e)
        db.rollback()
        return { 'created': False }
    finally:
        db.close()

def update_article(id, article):

    try:
        db = get_db()
        cursor = db.cursor()
        query = """
        UPDATE article
            SET titulo = ?,
            cuerpo = ?,
            fechaPublicacion = ?,
            categoria = ?,
            etiqueta = ?
        WHERE
            id = ?;
        
        """
        now = Date.today()
        cursor.execute(query, [article['titulo'], article['cuerpo'], now, article['categoria'], article['etiqueta'], id])
        db.commit()
        return { 'created': True }
    except Exception as e:
        print(e)
        db.rollback()
        return { 'created': False }
    finally:
        db.close()

def delete_article(id: int):
    try:
        db = get_db()
        cursor = db.cursor()
        query = "DELETE FROM article where id = ?"
        cursor.execute(query, [id])
        db.commit()
        return { 'deleted': True }
    except Exception as e:
        print(e)
        db.rollback()
        return { 'created': False }
    finally:
        db.close()

def parse_row(row):
    print(row)
    dict = {
        'id': row[0],
        'titulo': row[1],
        'cuerpo': row[2],
        'fechaDePublicacion': row[3],
        'etiqueta': row[4],
        'categoria': row[5]
    }
    return dict