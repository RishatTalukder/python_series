# ==========================
# HANDLING ERRORS
# ==========================

def divide(a, b):

    try:
        a = int(a)
        b = int(b)

        return a / b

    except (ValueError, ZeroDivisionError):
        print("Please enter valid numbers.")


while True:

    a = input("Enter the first number: ")

    if a == "q":
        break

    b = input("Enter the second number: ")

    if b == "q":
        break

    result = divide(a, b)

    if result is not None:
        print(result)


# ==========================
# HOMEWORK
# ==========================

# 1. Ask the user for two numbers and add them together.
#    Use try-except to handle invalid input.


# 2. Put the addition program inside a while loop so
#    the user can keep entering numbers even after
#    making a mistake.
#
#    Allow the user to enter "q" to quit.


# 3. Create two files:
#    cats.txt
#    dogs.txt
#
#    Put at least three animal names in each file.
#    Write a program that reads both files and prints
#    their contents.
#
#    Handle FileNotFoundError if a file is missing.


# 4. Modify the previous program so that it silently
#    ignores a missing file.


# 5. Find a text file containing a book or another
#    large piece of text.
#
#    Read the file and count how many times "the"
#    appears in the text.
#
#    Convert the text to lowercase before counting.
#    Also try counting "the " with a space and compare
#    the results.