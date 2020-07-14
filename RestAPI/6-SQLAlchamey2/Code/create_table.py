import sqlite3
import os

path = "/Users/tuncutku/Desktop/Courses/RestAPI/5-SQLAlchamey/Code/"

os.chdir(path)

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
cursor.execute(create_table)

connection.commit()
connection.close()
