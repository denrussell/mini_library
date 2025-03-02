import mysql.connector
from mysql.connector import Error

db_name = "e_commerce_db"
user = "root"
password = "burnek2433"
host = "localhost"

try:
    conn = mysql.connector.connect(
        database = db_name,
        user = user,
        password = password,
        host = host

    )
    if conn.is_connected():
        print("Successfully connected!")

except Error as e:
    print(f"Error: {e}")

finally:
    if conn and conn.is_connected():
        conn.close()
        print("MySQL connection is closed.")
