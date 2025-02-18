###### PART 1 #######

''' 
🎯 Functions Challenge: Library Management System
-------------------------------------------------

Your task is to implement a set of functions to manage a simple library system.
Follow the instructions below to complete the challenge.
'''

# 1️⃣ Function: add_book
# - Takes a dictionary (library), a book title, and an author.
# - Adds the book to the dictionary (title as key, author as value).
# - Returns the updated library.

ux_library = {"Python for Beginners": "Jane Doe",
    "The Adventures of Sherlock Holmes": "Arthur Conan Doyle",
    "War and Peace": "Leo Tolstoy"}

def add_book(library, title, author):
    library[title] = author
    return library
add_book(ux_library, "Ducker", "Quincy Quack")

# 2️⃣ Function: remove_book
# - Removes a book from the dictionary.
# - If the book does not exist, print "Book not found!".

def remove_book(library, title):
    if title in library:
        del library[title]
    else:
        print("Book not found!")
remove_book(ux_library, "Ducker")

# 3️⃣ Function: find_author
# - Takes the library dictionary and a title.
# - Returns the author's name if the book exists, otherwise "Book not found".

#that was tricky because I tried to check if there is element library[title] but it returns KeyError, so GET is the solution! In JS it would return undefined which means false


def find_author(library, title):
    author = library.get(title)
    if author:
        return author
    else:
        return "Book not found"

# 4️⃣ Function: list_books
# - Prints all books in the format: "Title: <title>, Author: <author>"

# .items was something new to me useful for key, value looping

def list_books(library):
    for title, author in library.items():
        print(f"Title: {title}, Author: {author}")
list_books(ux_library)

''' 
✅ Bonus Challenges (Optional)
--------------------------------
- Modify add_book() so it doesn’t overwrite existing books but prints "Book already exists!".
- Allow books to have multiple authors (Hint: store authors as a list).
- Add a function count_books(library) that returns the total number of books.
'''
def add_book(library, title, author):
    if title in library:
        print("Book already exists!")
        if author in library[title]:
            print("This author already exists for this book!")
        else:
            library[title].append(author)     
    else:
        library[title] = [author]   

    return library

add_book(ux_library, "Ducker", "Quincy Quack")

def count_books(library): 
    return len(library)



###### PART 2 #######

#1️⃣ Reverse a String
#Write a function reverse_string(text) that takes a string and returns it reversed.

def reverse_string(text):
    return text[::-1]

reverse_string('hello')

#2️⃣ Count Vowels
#Write a function count_vowels(text) that returns the number of vowels (a, e, i, o, u) in a given string.

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for letter in text:
        if letter in vowels:
            count += 1
    return count
count_vowels("Hello aIeO")

#3️⃣ Find the Maximum Number
#Write a function find_max(num1, num2, num3) that returns the largest of three numbers.

def find_max(*nums):
    max_number = float("-inf")
    for num in nums: 
        if isinstance(num, (int, float)) and num > max_number:
            max_number = num
    return max_number