class User:
    

    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    def get_user_details(self):
        return {
            "Name" : self.__name,
            "Library_ID" : self.__library_id,
            "Borrowed_Books" : self.__borrowed_books,
        }
    
    def borrow_book(self, book_title):
        if book_title not in self.__borrowed_books:
            self.__borrowed_books.append(book_title)

    def return_book(self, book_title):
        if book_title in self.__borrowed_books:
            self.__borrowed_books.remove(book_title)
    
def add_user(users):
    name = input("Enter user's name: ")
    library_id = input("Enter the user's library ID: ")

    if library_id in users:
        print("User already exists.")
    else:
        user = User(name, library_id)
        users[library_id] = user
        print(f"\nUser '{name}' has been added successfully.")
    
def display_all_users(users):
    if not users:
        print(">>>> No users in the system.")
    else:
        print("\nAll Registered Users:")
        for library_id, user in users.items():
            details = user.get_user_details()
            print(f"Name: {details['Name']} | Library ID: {details['Library_ID']} | Borrowed Books: {', '.join(details['Borrowed_Books']) if details['Borrowed_Books'] else 'None'}")
    
    
    '''
    def borrow_book(self, book_title):
        if book_title not in self.__borrowed_books:
            self.__borrowed_books.append(book_title)

    def return_book(self, book_title):
        if book_title in self.__borrowed_books:
            self.__borrowed_books.remove(book_title)
            '''