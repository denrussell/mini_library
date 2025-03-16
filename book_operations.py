def add_book(db):
    """Inserts a new book into the MySQL database."""
    title = input("Enter the title of the book: ")
    author_id = input("Enter the author's ID: ")  # Make sure author exists in the database

    # Check if the author exists
    cursor = db.connection.cursor()
    cursor.execute("SELECT id FROM authors WHERE id = %s", (author_id,))
    author_exists = cursor.fetchone()

    if not author_exists:
        print(f"\nAuthor ID {author_id} does not exist. Please add the author first!")
        return  # Stop the function and ask the user to add the author first

    isbn = input("Enter the ISBN (13 digits): ")  # Ensure ISBN is provided
    genre = input("Enter the genre: ")
    publication_date = input("Enter the publication date (YYYY-MM-DD): ")

    try:
        query = "INSERT INTO books (title, author_id, isbn, genre, publication_date) VALUES (%s, %s, %s, %s, %s)"
        values = (title, author_id, isbn, genre, publication_date)
        cursor.execute(query, values)
        db.connection.commit()
        print(f"\nBook '{title}' has been added successfully!")
    except Exception as e:
        print(f"⚠️ Error adding book: {e}")




def display_all_books(db):
    """Fetches and displays all books from the MySQL database."""
    try:
        query = "SELECT books.id, books.title, authors.name, books.genre, books.publication_date, books.availability FROM books JOIN authors ON books.author_id = authors.id"
        cursor = db.connection.cursor()
        cursor.execute(query)
        books = cursor.fetchall()

        if not books:
            print("\n>>>> No books available in the library.")
            return

        print("\nAll Books in Library:\n")
        for book in books:
            book_id, title, author, genre, publication_date, availability = book
            print(f"ID: {book_id}")
            print(f"Title: {title}")
            print(f"Author: {author}")
            print(f"Genre: {genre}")
            print(f"Publication Date: {publication_date}")
            print(f"Available: {'Yes' if availability else 'No'}")
            print("-" * 40)
    except Exception as e:
        print(f"Error retrieving books: {e}")

def borrow_book(db):
    """Allows a user to borrow a book by updating availability in the database."""
    book_id = input("Enter the book ID to borrow: ")
    
    try:
        # Check if the book is available
        cursor = db.connection.cursor()
        cursor.execute("SELECT availability FROM books WHERE id = %s", (book_id,))
        result = cursor.fetchone()

        if result is None:
            print("Book not found.")
        elif result[0] == 0:
            print("Sorry, this book is already borrowed.")
        else:
            # Mark the book as borrowed (availability = 0)
            cursor.execute("UPDATE books SET availability = 0 WHERE id = %s", (book_id,))
            db.connection.commit()
            print("Book borrowed successfully.")
    
    except Exception as e:
        print(f"Error borrowing book: {e}")

def return_book(db):
    """Allows a user to return a book by updating availability in the database."""
    book_id = input("Enter the book ID to return: ")

    try:
        cursor = db.connection.cursor()
        cursor.execute("SELECT availability FROM books WHERE id = %s", (book_id,))
        result = cursor.fetchone()

        if result is None:
            print("Book not found.")
        elif result[0] == 1:
            print("This book is already available.")
        else:
            # Mark the book as available (availability = 1)
            cursor.execute("UPDATE books SET availability = 1 WHERE id = %s", (book_id,))
            db.connection.commit()
            print("Book returned successfully.")
    
    except Exception as e:
        print(f"Error returning book: {e}")

def search_book(db):
    """Searches for a book in the database by title."""
    title = input("Enter the book title to search: ")

    try:
        cursor = db.connection.cursor()
        cursor.execute("SELECT books.id, books.title, authors.name, books.genre, books.publication_date, books.availability FROM books JOIN authors ON books.author_id = authors.id WHERE books.title LIKE %s", (f"%{title}%",))
        books = cursor.fetchall()

        if not books:
            print("No books found with that title.")
        else:
            print("\nSearch Results:")
            for book in books:
                book_id, title, author, genre, publication_date, availability = book
                print(f"ID: {book_id}")
                print(f"Title: {title}")
                print(f"Author: {author}")
                print(f"Genre: {genre}")
                print(f"Publication Date: {publication_date}")
                print(f"Available: {'Yes' if availability else 'No'}")
                print("-" * 40)
    
    except Exception as e:
        print(f"Error searching book: {e}")
