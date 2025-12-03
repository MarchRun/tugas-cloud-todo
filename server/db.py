import mysql.connector
import os
import time

def get_connection():
    retries = 5
    while retries > 0:
        try:
            connection = mysql.connector.connect(
                host=os.environ.get("DB_HOST", "localhost"),
                user=os.environ.get("DB_USER", "root"),
                password=os.environ.get("DB_PASSWORD", "261003"),
                database=os.environ.get("DB_NAME", "todo_db")
            )
            return connection
        except mysql.connector.Error as err:
            print(f"Gagal konek ke DB: {err}. Retrying in 5 seconds...")
            retries -= 1
            time.sleep(5)
    
    raise Exception("Tidak bisa terhubung ke Database setelah 5 kali percobaan.")