# ==========================
# DEFINING A FUNCTION
# ==========================

def display_message():
    print("I am learning about Python functions.")
    
# ==========================
# CALLING A FUNCTION
# ==========================

display_message()

# ==========================
# FUNCTION WITH A PARAMETER
# ==========================

def print_message(name):
    print(f"Welcome, {name.title()}!")
    print("Nice to meet you.")

print_message("rishat")
print_message("itvaya")

# ==========================
# USER INPUT + FUNCTION
# ==========================

def greet_user(name):
    print(f"Hello, {name.title()}!")

user_name = input("Enter your name: ")

greet_user(user_name)

# ==========================
# FAVORITE BOOK
# ==========================

def favorite_book(title):
    print(
        f"One of my favorite books is {title.title()}."
    )

favorite_book("alice in wonderland")
favorite_book("the alchemist")

# ==========================
# HOMEWORK
# ==========================

# 1. Write a function called display_message()
#    that prints one sentence about what you are
#    learning in Python.
#    Call the function.

# 2. Write a function called favorite_book(title)
#    that prints a sentence about your favorite book.
#    Call it with at least two different book titles.

# 3. Write a function called greet(name)
#    that prints a welcome message.
#    Call it with the names of three different people.

# 4. Write a function called favorite_food(food)
#    that prints:
#    "My favorite food is pizza."
#    Replace pizza with the argument passed to the function.

# 5. Ask the user for their name and pass it to
#    a greeting function.

# 6. Ask the user for their favorite game, movie,
#    or programming language and print a message
#    using a function.

# 7. Challenge:
#    Write a function called introduce(name, city)
#    that prints:
#    "My name is Rishat and I live in Dhaka."
#    Call the function with at least two different
#    sets of values.