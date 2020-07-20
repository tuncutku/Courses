from common.connection import get_cursor
from psycopg2.extras import Json

CREATE_ITEMS = """
CREATE TABLE IF NOT EXISTS items 
(id SERIAL PRIMARY KEY, url TEXT, tag_name TEXT, query JSONB, price NUMERIC);"""
SELECT_ITEMS = "SELECT url, tag_name, query, id FROM items"
INSERT_ITEM = "INSERT INTO items (url, tag_name, query, price) VALUES (%s, %s, %s, %s);"


def create_tables(connection):
    with get_cursor(connection) as cursor:
        cursor.execute(CREATE_ITEMS)


# -- items --
def get_items():
    with get_cursor() as cursor:
        cursor.execute(SELECT_ITEMS)
        return cursor.fetchall()


def insert_item(url, tag_name, query, price):
    with get_cursor() as cursor:
        cursor.execute(INSERT_ITEM, (url, tag_name, Json(query), price))

