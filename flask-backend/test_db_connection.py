import os
import pymysql  # Use PyMySQL instead of MySQLdb
from dotenv import load_dotenv

# Install PyMySQL as MySQLdb
pymysql.install_as_MySQLdb()

# Load environment variables from .env file
load_dotenv()

# Fetch environment variables
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DB = os.getenv('MYSQL_DB')

def test_db_connection():
    try:
        if not all([MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB]):
            raise ValueError("One or more environment variables are not set. Please check your .env file.")

        # Print environment variables to ensure they are loaded
        print(f"MYSQL_HOST: {MYSQL_HOST}")
        print(f"MYSQL_USER: {MYSQL_USER}")
        print(f"MYSQL_PASSWORD: {MYSQL_PASSWORD}")
        print(f"MYSQL_DB: {MYSQL_DB}")

        # Attempt to create a connection to the database
        connection = pymysql.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWORD,
            db=MYSQL_DB
        )

        print("Successfully connected to the database.")

        # Create a cursor object
        cursor = connection.cursor()

        # Execute a query to get the MySQL server version
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"MySQL Server Version: {version[0]}")

        # Print the IP address of the server
        print(f"MySQL Server IP Address: {MYSQL_HOST}")

        # Execute a query to get the list of databases
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()
        print("Databases on the server:")
        for db in databases:
            print(f"- {db[0]}")

        # Execute a simple query to test the connection
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        if result:
            print("Connection to the database was successful!")
        else:
            print("Connection to the database failed.")

        # Close the cursor and connection
        cursor.close()
        connection.close()

    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    test_db_connection()
