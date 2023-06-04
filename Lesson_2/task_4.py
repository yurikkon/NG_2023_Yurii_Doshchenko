library = {}
while True:
    print("Choose the operation from list:\n 1) Add new book\n 2) Delete book\n 3) Edit existing book\n 4) Find a book ")
    books = input("What operation you want choose?: ")
    match books:
        case "Add new book" | "1":
            print("Fill in information about the book:")
            book_name = input("Book title: ")
            book_author = input("Author: ")
            book_pages = int(input("Number of pages: "))
            book_ganr = input("Genre: ")
            book_cover = input("Book binding: ")


            book = {
                "Title": book_name,
                "Author": book_author,
                "Pages": book_pages,
                "Genre":  book_ganr,
                "Cover": book_cover
            }
            key = book_name
            library[key] = book

        case "Delete book" | "2":
            print(f"Books list: {list(library.keys())}")
            book_name = input("Enter the name of book you want to delete: ")
            del library[book_name]


        case "Edit existing book" | "3":
            editing_book = input(f"Choose the book from list {list(library.keys())}: ")
            parametr = input(f"Choose the param:\n {list(library[editing_book].keys())} ")
            new_value = input(f"Enter the new value of {parametr}: ")
            library[editing_book][parametr] = new_value
            print(f"Success!. The new value of {parametr} is '{new_value}'")


        case "Find a book" | "4":
            print(f'Book list: {list(library.keys())}')
            search_title = input("Enter the title of book you are interested in: ")
            if search_title in library.keys():
                print("The book was successfully found :)")
                print(library[search_title])
            else:
                print("Book with this title not found!!!")