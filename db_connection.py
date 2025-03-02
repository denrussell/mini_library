import mysql.connector  # Ensure you have mysql-connector installed

class Database:
    def __init__(self, host="localhost", user="root", password="burnek2433", database="library_db"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Database connected successfully!")
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL: {e}")

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
