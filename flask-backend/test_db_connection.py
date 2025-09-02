# flask-backend/test_db_connection.py

import os
import pymysql
from dotenv import load_dotenv

pymysql.install_as_MySQLdb()

load_dotenv()

MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DB = os.getenv('MYSQL_DB')

def test_db_connection():
    try:
        if not all([MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB]):
            raise ValueError("One or more environment variables are not set. Please check your .env file.")

        print(f"MYSQL_HOST: {MYSQL_HOST}")
        print(f"MYSQL_DB: {MYSQL_DB}")

        connection = pymysql.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWORD,
            db=MYSQL_DB  # 👈 this selects `core-full-stack` by default
        )

        print("Successfully connected to the database.")

        cursor = connection.cursor()

        # Show version
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"MySQL Server Version: {version[0]}")

        # Verify the active database
        cursor.execute("SELECT DATABASE()")
        active_db = cursor.fetchone()
        print(f"Currently using database: {active_db[0]}")

        # Show all tables in this DB
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        print("Tables in the database:")
        for table in tables:
            print(f"- {table[0]}")

        # Query the todos table
        print("\nTodos in the database:")
        cursor.execute("SELECT * FROM todos")
        todos = cursor.fetchall()
        for todo in todos:
            print(todo)  # each row is a tuple (id, title)

        cursor.close()
        connection.close()

    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    test_db_connection()
