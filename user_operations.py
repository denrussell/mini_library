from db_connection import Database

class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id

def add_user(db):
    """Inserts a new user into the MySQL database."""
    name = input("Enter user's name: ")
    library_id = input("Enter the user's library ID: ")

    try:
        cursor = db.connection.cursor()
        query = "INSERT INTO users (library_id, name) VALUES (%s, %s)"
        cursor.execute(query, (library_id, name))
        db.connection.commit()

        print(f"\nUser '{name}' with Library ID '{library_id}' has been added successfully.")
    
    except Exception as e:
        print(f"Error adding user: {e}")



def display_user_details(db):
    """Retrieves and displays a user's details based on their library ID."""
    library_id = input("Enter the User's Library ID: ")

    try:
        cursor = db.connection.cursor()
        query = "SELECT library_id, name FROM users WHERE library_id = %s"
        cursor.execute(query, (library_id,))
        user = cursor.fetchone()

        if user:
            print(f"\nUser Details:\nLibrary ID: {user[0]}\nName: {user[1]}")
        else:
            print("User not found.")

    except Exception as e:
        print(f"Error retrieving user details: {e}")


def view_user_details(db):
    """Fetches details of a specific user from the database."""
    if not db.connection:
        print("Error: Database connection not established.")
        return

    library_id = input("Enter the User's Library ID: ").strip()  

    try:
        cursor = db.connection.cursor()
        query = "SELECT library_id, name FROM users WHERE library_id = %s"
        cursor.execute(query, (library_id,))  
        user = cursor.fetchone()

        if user:  
            print(f"\nUser Details:\nLibrary ID: {user[0]} | Name: {user[1]}")
        else:
            print("User not found.")  
    except Exception as e:
        print(f"Error retrieving user details: {e}")


def display_all_users(db):
    """Fetches and displays all users from the database."""
    try:
        cursor = db.connection.cursor()
        query = "SELECT library_id, name FROM users"
        cursor.execute(query)
        users = cursor.fetchall()

        if not users:
            print("\n>>>> No users found in the system.")
            return

        print("\nAll Registered Users:\n")
        for user in users:
            print(f"Library ID: {user[0]} | Name: {user[1]}")
        print("-" * 40)

    except Exception as e:
        print(f"Error retrieving users: {e}")
