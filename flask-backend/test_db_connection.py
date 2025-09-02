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
        print(f"MYSQL_USER: {MYSQL_USER}")
        print(f"MYSQL_PASSWORD: {MYSQL_PASSWORD}")
        print(f"MYSQL_DB: {MYSQL_DB}")

        connection = pymysql.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWORD,
            db=MYSQL_DB
        )

        print("Successfully connected to the database.")

        cursor = connection.cursor()

        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"MySQL Server Version: {version[0]}")

        print(f"MySQL Server IP Address: {MYSQL_HOST}")

        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()
        print("Databases on the server:")
        for db in databases:
            print(f"- {db[0]}")

        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        if result:
            print("Connection to the database was successful!")
        else:
            print("Connection to the database failed.")

        cursor.close()
        connection.close()

    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    test_db_connection()
