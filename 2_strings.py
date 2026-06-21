# Declairing a string with single quotes or double quotes
name = 'itvaya talukder'

# some usefull methods of strings
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.title())

# Concatenation
first_name = "itvaya"
last_name = "talukder"
full_name = first_name + " " + last_name
print(full_name)

# f string
first_name = "itvaya"
last_name = "talukder"
marks = 100

full_name = f"Hello, {first_name} {last_name}. \n\tYou got {marks} marks."
print(full_name.title())

# stripping whitespace
name = "             itvaya                      haodfhoawihf        "
print(name.strip())
print(name.lstrip())
print(name.rstrip())

# Only use double quotes or single quotes
# If using single quotes, don't use single quotes inside the string
# Otherwise you have to make a new string from the point where you want to use single quotes
# And concatenate the strings
wrong_format = 'Hello, to ITVAYA's you tube channel"
right_format = "Hello, to ITVAYA's you tube channel"


# ==========================
# HOMEWORK
# ==========================

# 1. Create a variable called `name` and store your name in it.
#    Print a greeting message using that variable.
#    Example output:
#    Hello, Itvaya! Welcome to Python.

# 2. Create a string variable and print it in:
#    - lowercase
#    - UPPERCASE
#    - Title Case

# 3. Store your first name and last name in two separate variables.
#    Combine them into a full name and print the result.

# 4. Create an f-string that prints a short student report.
#    Include:
#    - first name
#    - last name
#    - a marks variable
#    Use \n and \t to format the output nicely.

# 5. Create a string with extra spaces at the beginning and end.
#    Print the original string, then print it using:
#    - strip()
#    - lstrip()
#    - rstrip()

# 6. Store your favorite quote in a variable and print it.
#    Also store the author's name in another variable and
#    display both in a single formatted sentence.

# 7. Create a string that contains an apostrophe (') correctly.
#    Try using both single quotes and double quotes, and
#    observe which one works without escaping the character.