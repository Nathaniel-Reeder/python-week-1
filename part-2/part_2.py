### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = ['Brandon Sanderson', 'JRR Tolkien', 'James S.A. Corey', 'George RR Martin', 'Rick Riordan', 'Susanne Collins', 'Glynn Stewart']

# Now let's add a new author to the end with the .append() method. Type your code below.

# Code here
# Example: my_authors.append("H.G. Wells")
my_authors.append('Claudia Grey')

# Now let's remove an element in the list

# Code here
# Example: my_authors.remove("H.G. Wells")
my_authors.remove('Claudia Grey')

# Now access an element by it's index. (Remember it indexes start at 0.)

# Code here
# Example: my_authors[2]
my_authors[5]

# Now slice the list.

# Code here
# Example: my_authors[1:4]
my_authors[0:3]

### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.

# Code here
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")
author_tuple = ('Brandon Sanderson', 'JRR Tolkien', 'James S.A. Corey', 'George RR Martin', 'Rick Riordan', 'Susanne Collins', 'Glynn Stewart')

### Step 3 - Sets ###

# Create a set with your authors.

# Code here
# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}
author_set = {'Brandon Sanderson', 'JRR Tolkien', 'James S.A. Corey', 'George RR Martin', 'Rick Riordan', 'Susanne Collins', 'Glynn Stewart'}

# Add a new author to your set.

# Code here
# Example: my_author_set.add("J.R.R. Tolkien")
author_set.add('Claudia Grey')

# Try adding the same author again, and be sure to print your set.

# Code here
# Example: my_author_set.add("J.R.R. Tolkien")
print(author_set)
author_set.add('Claudia Grey')
print(author_set)

### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.

# Code here
# Example:

# for book in my_authors:
    # print(book)

for book in my_authors:
    print(book)

# for book in my_authors_tuple:
    # print(book)

for author in author_tuple:
    print(author)

# for book in my_authors_set:
    # print(book)

for author in author_set:
    print(author)