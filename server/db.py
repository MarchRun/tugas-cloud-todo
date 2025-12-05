import os
from google.cloud.sql.connector import Connector, IPTypes
import pymysql

connector = Connector()

def get_connection():
    conn = connector.connect(
        os.environ["DB_INSTANCE"],  # instance connection name
        "pymysql",
        user=os.environ.get("DB_USER", "root"),
        password=os.environ.get("DB_PASSWORD", ""),
        db=os.environ.get("DB_NAME", "todo_db"),
        ip_type=IPTypes.PRIVATE
    )
    return conn
