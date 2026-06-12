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
