import mysql.connector

class Database:
    def __init__(self, host="localhost", user="root", password="burnek2433", database="library_db"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Database connected successfully!")
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL: {e}")

    def close(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Database connection closed.")

    # Insert a book into the database
    def add_book(self, title, author_id, isbn, publication_date, availability=True):
        query = "INSERT INTO books (title, author_id, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s)"
        values = (title, author_id, isbn, publication_date, availability)
        self.cursor.execute(query, values)
        self.connection.commit()
        print(f"Book '{title}' added successfully.")

    # Fetch all books from the database
    def get_all_books(self):
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()

    # Find a book by title
    def search_book(self, title):
        query = "SELECT * FROM books WHERE title = %s"
        self.cursor.execute(query, (title,))
        return self.cursor.fetchone()

    # Update book availability (borrow/return)
    def update_book_availability(self, book_id, availability):
        query = "UPDATE books SET availability = %s WHERE id = %s"
        self.cursor.execute(query, (availability, book_id))
        self.connection.commit()
        print(f"Book with ID {book_id} updated.")

    # Delete a book
    def delete_book(self, book_id):
        query = "DELETE FROM books WHERE id = %s"
        self.cursor.execute(query, (book_id,))
        self.connection.commit()
        print(f"Book with ID {book_id} deleted.")
