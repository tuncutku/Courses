from common.connection import get_cursor
from psycopg2.extras import Json

CREATE_ITEMS = """
CREATE TABLE IF NOT EXISTS items 
(id SERIAL PRIMARY KEY, url TEXT, tag_name TEXT, query JSONB);"""
CREATE_ALERTS = """
CREATE TABLE IF NOT EXISTS alerts (
    id SERIAL PRIMARY KEY, item_id INTEGER, price_limit NUMERIC,
    FOREIGN KEY(item_id) REFERENCES items(id)
);"""

SELECT_ITEMS = "SELECT url, tag_name, query, id FROM items"
SELECT_ITEM = "SELECT url, tag_name, query, id FROM items WHERE id = %s;"
SELECT_ALERTS = "SELECT item_id, price_limit, id FROM alerts"
SELECT_ALERT = "SELECT item_id, price_limit, id FROM alerts WHERE item_id = %s"


INSERT_ITEM = "INSERT INTO items (url, tag_name, query) VALUES (%s, %s, %s);"

CREATE_ALERTS = """CREATE TABLE IF NOT EXISTS items 
(id SERIAL PRIMARY KEY, url TEXT, tag_name TEXT, query JSONB, price NUMERIC);"""


class Database:
    @staticmethod
    def create_tables():
        with get_cursor() as cursor:
            cursor.execute(CREATE_ITEMS)

    @staticmethod
    def insert_item(url, tag_name, query):
        with get_cursor() as cursor:
            cursor.execute(INSERT_ITEM, (url, tag_name, Json(query)))

    @staticmethod
    def insert_alert(item_id, price_limit):
        with get_cursor() as cursor:
            cursor.execute(INSERT_ALERT, (item_id, price_limit))

    @staticmethod
    def get_one(collection, item_id):
        with get_cursor() as cursor:
            if collection == "item":
                cursor.execute(SELECT_ITEM, item_id)
                return cursor.fetchone()
            else:
                cursor.execute(SELECT_ALERT, item_id)
                return cursor.fetchone()

    @staticmethod
    def get_all(collection):
        with get_cursor() as cursor:
            if collection == "item":
                cursor.execute(SELECT_ITEMS)
                return cursor.fetchall()
            else:
                cursor.execute(SELECT_ALERTS)
                return cursor.fetchall()

