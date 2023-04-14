my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

my_book_2 = {
    "title": "Leviathan Wakes",
    "author": "James S.A. Corey",
    "year": 2017,
    "rating": 4.6,
    "pages":543
}

my_book_3 = {
    "title": "Catching Fire",
    "author": "Suzanne Collins",
    "year": 2010,
    "rating": 4.02,
    "pages": 389
}

library_list = [my_book, my_book_2, my_book_3]

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def describe_book(book_dict):
    book_description = f"The book's title is {book_dict['title']} and the author is {book_dict['author']}. It was released in {book_dict['year']} and is rated {book_dict['rating']}. It has {book_dict['pages']} pages."
    return book_description

print(describe_book(my_book))

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

def get_title(book_dict):
    return book_dict['title']

def get_author(book_dict):
    return book_dict['author']

def get_year(book_dict):
    return book_dict['year']

def get_rating(book_dict):
    return book_dict['rating']

def get_pages(book_dict):
    return book_dict['pages']

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def get_by_author(book_list, author):
    by_author = []
    for book in book_list:
        if book['author'] == author:
            by_author.append(book)
        else:
            pass
    return by_author

print(get_by_author(library_list, "Suzanne Collins"))

def count_books(book_list):
    book_count = 0
    for book in book_list:
        book_count += 1
    return book_count

print(count_books(library_list))

def more_pages(book_list, pages):
    big_book_list = []
    for book in book_list:
        if book['pages'] > pages:
            big_book_list.append(book)
        else:
            pass
    if big_book_list == []:
        return "No books with more pages were found."
    else:
        return big_book_list
    
print(more_pages(library_list, 400))
