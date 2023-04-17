### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here

def create_new_book_old():
    title = input("What is the title of the book you would like to add? - ")
    author = input("Who is the author of the book you would like to add? - ")
    year = input("What year was this book published? - ")
    rating = input("What rating out of 5 would you give this book? - ")
    pages = input("What is the page count of the book? - ")

    book_dict = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return book_dict

# print(create_new_book())

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

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

### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

#Added to the function above

### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

first_book = {
    "title": "Leviathan Wakes",
    "author": "James S.A. Corey",
    "year": 2011,
    "rating": 4.7,
    "pages": 577    
}

second_book = {
    "title": "The Way of Kings",
    "author": "Brandon Sanderson",
    "year": 2010,
    "rating": 4.8,
    "pages": 1007
}

third_book = {
    "title": "A Game of Thrones",
    "author": "George R.R. Martin",
    "year": 1996,
    "rating": 4.2,
    "pages": 694
}

book_list = [first_book, second_book, third_book]

def describe_book(book_dict):
    book_description = f"Title: {book_dict['title']} \nAuthor: {book_dict['author']} \nReleased in: {book_dict['year']} \nRating: {book_dict['rating']} \nPages: {book_dict['pages']}"
    return book_description


def main_menu():
    to_do = input("To add a new book, type 'Add'. To see all books in the library, type 'See All Books'. To exit, type 'Exit'.")

    if to_do == 'Add':
        new_book = create_new_book()
        book_list.append(new_book)
        print('New book added!')
    elif to_do == 'See All Books':
        for book in book_list:
            print(describe_book(book))
    # elif to_do == 'Exit':
    #     # break
    else:
        print('The response received was not accepted. Please try again.')

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

while 1 == 1: 
    to_do = input("To add a new book, type 'Add'. To see all books in the library, type 'See All Books'. To exit, type 'Exit'.  ")
    print(to_do)
    if to_do == 'Add':
        print('\n')
        new_book = create_new_book()
        book_list.append(new_book)
        print('New book added!')
        print('\n')
    elif to_do == 'See All Books':
        print('\n')
        for book in book_list:
            print(describe_book(book))
            print('\n')
    elif to_do == 'Exit':
        break
    else:
        print('\nThe response received was not accepted. Please try again.')

        