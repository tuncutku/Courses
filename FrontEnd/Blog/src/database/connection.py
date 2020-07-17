from contextlib import contextmanager
from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()
database_uri = os.environ["DATABASE_URI"]
connection = psycopg2.connect(database_uri)


@contextmanager
def get_cursor():
    with connection:
        with connection.cursor() as cursor:
            yield cursor
