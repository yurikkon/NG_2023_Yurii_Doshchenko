global library
library = {}


def main():
    while True:
        print("Choose the operation from list:\n [1] Add book\n [2] Delete book\n [3] Edit existing book"
              "\n [4] Find book ")
        operation = input("Chosen operation: ")
        match operation:
            case "Add new book" | "1":
                new_book()
            case "Delete book" | "2":
                delete_book()
            case "Edit existing book" | "3":
                edit_book()
            case "Find a book" | "4":
                find_book()

def new_book():
    print("Fill in information about the book:")
    Name = input("Book title: ")
    Author_ThisBook = input("Author: ")
    NumberOf_Pages = int(input("Number of pages: "))
    Genre = input("Genre: ")
    Cover = input("Book cover: ")
    print()
    book = {
        "Title": Name,
        "Author": Author_ThisBook,
        "Pages": NumberOf_Pages,
        "Genre": Genre,
        "Cover": Cover

    }
    key = Name
    library[key] = book

def delete_book():
    print(f"Book list: {list(library.keys())} ")
    book_title = input("Enter the title of book you want to delete: ")
    if book_title in library.keys():
        del library[book_title]
        print(f"Success. Book with title {book_title} was deleted :) ")
    else:
        print("Error. Book with this title not found :( ")
    print()

def edit_book():
    editing_book = input(f"Choose the book from list {list(library.keys())}: ")
    arguments = input(f"Choose the param:\n {list(library[editing_book].keys())} ")
    new_value = input(f"Enter the new value of {arguments}: ")
    library[editing_book][arguments] = new_value
    print(f"Success!. The new value of {arguments} is '{new_value}'")

def find_book():
    print(f'Book list: {list(library.keys())}')
    search_title = input("Enter the title of book you are interested in: ")
    if search_title in library.keys():
        print("The book was successfully found!")
        print(library[search_title])
    else:
        print("Error. Book not found!!")
    print()

main()