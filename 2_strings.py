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


# HOMEWORK

# Use a variable to represent a person’s name, and print
# a message to that person. Your message should be simple, such as, “Hello Eric,
# would you like to learn some Python today?”

# Use a variable to represent a person’s name, and then print
# that person’s name in lowercase, uppercase, and title case.

# Find a quote from a famous person you admire. Print the
# quote and the name of its author. Your output should look something like the
# following, including the quotation marks:
# Albert Einstein once said, “A person who never made a
# mistake never tried anything new.”

# Repeat Exercise 2-5, but this time, represent the
# famous person’s name using a variable called famous_person. Then compose
# your ­message and represent it with a new variable called message. Print your
# message.

# Use a variable to represent a person’s name, and include
# some whitespace characters at the beginning and end of the name. Make sure
# you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().  
