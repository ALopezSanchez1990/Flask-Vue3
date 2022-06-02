import json
import sqlite3
from unicodedata import category
from unittest import result
from db.db import get_db

def get_all_categories():
    db = get_db()
    cursor = db.cursor()
    query = "Select id, title from category"
    categories = cursor.execute(query).fetchall()
    results = {
        'categories': []
    }

    [results['categories'].append(parse_row(category)) for category in categories]

    db.close()
    return results

def create_article():
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO article(titulo, cuerpo, fechaPublicacion, categoria, etiqueta) VALUES (?, ?, ?, ? , ?)"
    cursor.execute(query, [])
    return cursor.fetchall()['id']

def parse_row(row):
    dict = {
        'id': row[0],
        'title': row[1]
    }
    return dict