# This will hold all operations related to books

class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__is_available = True

    def get_details(self):
        return {
            "Title": self.__title,
            "Author": self.__author,
            "Genre": self.__genre,
            "Publication Date": self.__publication_date,
            "Available": self.__is_available,
        }

    def borrow_book(self):
        if self.__is_available:
            self.__is_available = False
            return True
        return False

    def return_book(self):
        self.__is_available = True

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author



def add_book(library, authors):
    title = input("Enter the title of the book: ")
    author = input("Enter the name of the author: ")
    genre = input("Enter the genre: ")
    publication_date = input("Enter the publication date: ")

    if author not in authors:
        print(f"Author does not exist. Please add author first.")
        return

    if title in library:
        print("Book already exists in the library.")
    else:
        book = Book(title, author, genre, publication_date)  
        library[title] = book
        print(f"\n>>>> Book '{title}' by {author} has been added successfully.")


def display_all_books(library):
    if not library:
        print("\n>>>> No books available in the library.")
    else:
        print("\nAll books in the library:\n")
        for title, book in library.items():
            details = book.get_details()
            print(f"Title: {details['Title']}")
            print(f"Genre: {details['Genre']}")
            print(f"Publication Date: {details['Publication Date']}")
            print(f"Author: {details['Author']}")
            print(f"Available: {'Yes' if details['Available'] else 'No'}")
            print("-" * 40)
