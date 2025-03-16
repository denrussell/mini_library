from db_connection import Database

class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

def add_author(db):
    """Inserts a new author into the database and displays their assigned ID."""
    name = input("Enter author's name: ")
    biography = input("Enter author's biography: ")

    try:
        query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
        values = (name, biography)
        cursor = db.connection.cursor()
        cursor.execute(query, values)
        db.connection.commit()

        
        author_id = cursor.lastrowid
        print(f"\nAuthor '{name}' added successfully! Assigned ID: {author_id}")
    except Exception as e:
        print(f"⚠️ Error adding author: {e}")


def display_all_authors(db):
    """Fetches and displays all authors from the MySQL database."""
    try:
        query = "SELECT id, name, biography FROM authors"
        cursor = db.connection.cursor()
        cursor.execute(query)
        authors = cursor.fetchall()

        if not authors:
            print("\n>>>> No authors in the system.")
            return

        print("\nAll Recorded Authors:\n")
        for author in authors:
            author_id, name, biography = author
            print(f"ID: {author_id} | Name: {name} | Biography: {biography}")
            print("-" * 40)
    except Exception as e:
        print(f"Error retrieving authors: {e}")


def get_author_details(db):
    """Fetch and display details of an author from the database."""
    name = input("Enter the author's name: ")

    try:
        query = "SELECT id, name, biography FROM authors WHERE name = %s"
        cursor = db.connection.cursor()
        cursor.execute(query, (name,))
        author = cursor.fetchone()

        if author:
            author_id, author_name, biography = author
            print("\nAuthor Details:")
            print(f"ID: {author_id}")
            print(f"Name: {author_name}")
            print(f"Biography: {biography}")
        else:
            print("⚠️ Author not found.")

    except Exception as e:
        print(f"Error retrieving author details: {e}")

