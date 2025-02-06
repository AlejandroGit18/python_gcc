import pyodbc
from app.config import settings

def get_db_connection():
    try:
        connection = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={settings.DB_SERVER},{settings.DB_PORT};"
            f"DATABASE={settings.DB_NAME};"
            f"UID={settings.DB_USER};"
            f"PWD={settings.DB_PASSWORD}"
        )
        return connection
    except pyodbc.Error as e:
        print(f"Database connection error: {e}")
        raise
