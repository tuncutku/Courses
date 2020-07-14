import sqlite3

connection = sqlite3.connect("data.db")
connection.row_factory = sqlite3.Row  # gives dictionary instead of tuple


def create_table():
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);"
        )


def add_entry(entry_content, entry_date):
    with connection:
        connection.execute(
            "INSERT INTO entries VALUES (?, ?);", (entry_content, entry_date)
        )


def get_entries():
    cursor = connection.execute("SELECT * FROM entries")
    # cursor.fetchone() # gives the first value
    return cursor
