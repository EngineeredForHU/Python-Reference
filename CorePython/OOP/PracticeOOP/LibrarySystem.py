#8/16/2025

class Book:
    # Start of the unique ID
    book_id = 1
    # Constructor
    def __init__(self, book_name, author, pages):
        self.book_name = book_name
        self.author = author
        self.pages = pages
        self.id = Book.book_id
        Book.book_id += 1


    # Basic method that gets the name of the book
    def get_name(self):
        return f"{self.book_name}"

    # the description of the object(Book) that is being called
    def __str__(self):
        return f"ID# [{self.id}] - Title: {self.book_name}. \nAuthor: {self.author}. ({self.pages} pages)\n"

# Holds thw books
def bookstore():
    return [
        Book("Harry Potter: The Sorcerer Stone", "J.K Rowling",498),
        Book("Linear Algebra", "Howard Anton",643),
        Book("The C Programming language", "Dennis Richie",487)
    ]

# Shows the menu
def show_menu():
    print("MENU:")
    print("1. Show available books")
    print("Q. Quit")

# Main function
def main():
    inventory = bookstore()
    while True:
        show_menu()
        choice = input("What operation would you like to perform? ").strip().lower()
        if choice == "1":
            if not inventory:
                print("No books in inventory.")
            else:
                print("\nAvailable Books:")
                for book in inventory:
                    print(book)
        else:
            break

if __name__ == "__main__":
    main()