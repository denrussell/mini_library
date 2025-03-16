from db_connection import Database
from book_operations import add_book, display_all_books, borrow_book, return_book, search_book
from user_operations import add_user, display_all_users, view_user_details
from author_operations import add_author, display_all_authors, get_author_details
from user_interface import main_menu, book_menu, user_menu, author_menu

def main():
    db = Database(password="burnek2433")  # Connect to MySQL

    while True:
        main_menu()
        choice = input("Enter choice number: ")

        if choice == "1":
            while True:
                book_menu()
                book_choice = input("Enter choice number: ")
                if book_choice == "1":
                    add_book(db)
                elif book_choice == "2":
                    borrow_book(db) 
                elif book_choice == "3":
                    return_book(db) 
                elif book_choice == "4":
                    search_book(db) 
                elif book_choice == "5":
                    display_all_books(db)
                elif book_choice == "6":
                    print("Returning to the Main Menu...")
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "2":
            while True:
                user_menu()
                user_choice = input("Enter choice number: ")
                if user_choice == "1":
                    add_user(db)
                elif user_choice == "2":
                    view_user_details(db)
                elif user_choice == "3":
                    display_all_users(db)
                elif user_choice == "4":
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "3":  # Author Operations
            while True:
                author_menu()
                author_choice = input("Enter choice number: ")
                if author_choice == "1":
                    add_author(db)
                elif author_choice == "2":  
                    get_author_details(db)  
                elif author_choice == "3":
                    display_all_authors(db)
                elif author_choice == "4":
                    break
                else:
                    print("Invalid choice. Please try again.")


        elif choice == "4":
            print("Exiting...")
            db.close()
            break

if __name__ == "__main__":
    main()
