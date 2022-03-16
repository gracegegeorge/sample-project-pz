import os
from psycopg import connect, OperationalError


def create_connection():
    try:
        conn = connect(
            host=os.environ.get("Host"),
            dbname=os.environ.get("DB"),
            user=os.environ.get("USER"),
            password=os.environ.get("PASSWORD"),
            port=os.environ.get("PORT")
        )

        return conn

    except OperationalError as oe:
        print(oe)

        return "Could not connect to the database"


connection = create_connection()

print(connection)
