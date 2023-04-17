### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here

def create_new_book():
    title = input("What is the title of the book you would like to add? - ")
    author = input("Who is the author of the book you would like to add? - ")
    try:
        year = int(input("What year was this book published? - "))
    except:
        year = int(input("Please type a number for the year?"))
    try:
        rating = float(input("What rating out of 5 would you give this book? - "))
    except:
        rating = float(input("Please enter a decimal for your rating out of five."))
    try:
        pages = int(input("What is the page count of the book? - "))
    except:
        pages = int(input("Please enter a number for the pages in the book."))

    book_dict = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return book_dict

def add_book(book_dict):
    with open("library.txt", "a") as f:
        f.write(f"{book_dict['title']}, {book_dict['author']}, {book_dict['year']}, {book_dict['rating']}, {book_dict['pages']}\n")

first_book = {
    "title": "Leviathan Wakes",
    "author": "James S.A. Corey",
    "year": 2011,
    "rating": 4.7,
    "pages": 577    
}

# add_book(first_book)

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

def describe_book(book_dict):
    book_description = f"Title: {book_dict['title']} \nAuthor: {book_dict['author']} \nReleased in: {book_dict['year']} \nRating: {book_dict['rating']} \nPages: {book_dict['pages']}"
    return book_description

# Code here

def display_all_book_info():
    with open("library.txt", 'r') as f:
        file = f.readlines()
        for line in file:
            title, author, year, rating, pages = line.split(", ")

            book_dictionary = {
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            }

            print(describe_book(book_dictionary))
            print('\n')



### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!


def all_pages():
    page_count = 0
    with open("library.txt", 'r') as f:
        file = f.readlines()
        for line in file:
            title, author, year, rating, pages = line.split(", ")

            book_dictionary = {
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            }
            page_count += book_dictionary["pages"]
        return page_count
    
def average_rating():
    book_count = 0
    rating_total = 0
    with open("library.txt", 'r') as f:
        file = f.readlines()
        for line in file:
            title, author, year, rating, pages = line.split(", ")

            book_dictionary = {
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            }

            book_count += 1
            rating_total += book_dictionary["rating"]
    return rating_total / book_count

def get_by_author():
    books_by_author = []
    author_name = input("Please type the author's name.  ")
    with open("library.txt", 'r') as f:
        file = f.readlines()
        for line in file:
            title, author, year, rating, pages = line.split(", ")

            book_dictionary = {
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            }

            if book_dictionary["author"] == author_name:
                books_by_author.append(book_dictionary)
    if books_by_author != []:
        print('\n')
        for book in books_by_author:
            print(describe_book(book))
            print('\n')
    else:
        print('\nNo books found under that author. Make sure it was spelled correctly.\n')



if __name__ == "__main__":
    while 1 == 1: 
        to_do = input("To add a new book, type 'Add'. To see all books in the library, type 'See All Books'. To see total pages, type 'Pages'. To see average rating of all books, type 'Rating'. To get all books by author, type 'Author'. To exit, type 'Exit'.\n\n")

        to_do = to_do.lower()
        
        if to_do == 'add':
            print('\n')
            add_book(create_new_book())
            print('\nNew book added!\n')
        elif to_do == 'see all books':
            print('\n')
            display_all_book_info()
        elif to_do == 'pages':
            print('\n')
            print(all_pages())
            print('\n')
        elif to_do == 'rating':
            print('\n')
            print(average_rating())
            print('\n')
        elif to_do == 'author':
            print('\n')
            get_by_author()
        elif to_do == 'exit':
            break
        else:
            print('\nThe response received was not accepted. Please try again.')
