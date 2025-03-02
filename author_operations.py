# This will hold all operations related to authors

class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def get_details(self):
        return {
            "Name" : self.__name,
            "Biography" : self.__biography,
        }

def get_author_details(authors):
    name = input("Enter the author's name: ")
    if name in authors:
        author = authors[name]
        details = author.get_details()
        print(f"Name: {details['Name']}")
        print(f"Biography: {details['Biography']}")
    else:
        print("Author not found.")

def add_author(authors):
    name = input("Enter author's name: ")
    biography = input("Enter author's biography: ")

    if name in authors:
        print("Author already exists.")
    else:
        author = Author(name, biography)
        authors[name] = author
        print(f"\nAuthor '{name}' has been added successfully.")
    
def display_all_authors(authors):
    if not authors:
        print(">>>> No authors in the system.")
    else:
        print("\nAll Recorded Authors:")
        for name, author in authors.items():
            details = author.get_details()
            print(f"Name: {details['Name']} | Biography: {details['Biography']}")
    