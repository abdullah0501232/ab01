import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST") or os.getenv("MYSQL_HOST", "localhost"),
            user=os.getenv("DB_USER") or os.getenv("MYSQL_USER", "root"),
            password=os.getenv("DB_PASSWORD") or os.getenv("MYSQL_PASSWORD", ""),
            database=os.getenv("DB_NAME") or os.getenv("MYSQL_DATABASE", "job_tracker"),
            port=int(os.getenv("DB_PORT") or os.getenv("MYSQL_PORT", 3306))
        )
        return connection

    except Error as e:
        print("Database connection error:", e)
        return None