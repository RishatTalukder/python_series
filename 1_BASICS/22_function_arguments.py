# ==========================
# FUNCTION WITH DEFAULT VALUES
# ==========================

def power(num=0, power_value=0):
    print(f"Number : {num}")
    print(f"Result : {num ** power_value}")


# Calling without arguments
power()

# Calling with one positional argument
power(5)

# Calling with two positional arguments
power(2, 3)

# Calling with a keyword argument
power(power_value=3)

# Calling with keyword arguments in any order
power(power_value=2, num=4)


# ==========================
# POSITIONAL ARGUMENTS
# ==========================

def greet(name, message):
    print(f"{message}, {name.title()}!")

greet("rishat", "Welcome")


# ==========================
# KEYWORD ARGUMENTS
# ==========================

greet(message="Hello", name="itvaya")


# ==========================
# T-SHIRT FUNCTION
# ==========================

def make_shirt(size, text):
    print(f"T-shirt size : {size}")
    print(f"Message       : {text}")

# Positional arguments
make_shirt("Large", "Code Everyday")

# Keyword arguments
make_shirt(text="Python Lover", size="Medium")


# ==========================
# LARGE SHIRTS WITH DEFAULTS
# ==========================

def make_shirt_default(size="Large", text="I love Python"):
    print(f"T-shirt size : {size}")
    print(f"Message       : {text}")

# Large shirt with default message
make_shirt_default()

# Medium shirt with default message
make_shirt_default(size="Medium")

# Custom shirt
make_shirt_default(size="Small", text="Build Projects")


# ==========================
# CITY DESCRIPTION
# ==========================

def describe_city(city, country="Bangladesh"):
    print(f"{city.title()} is in {country.title()}.")

describe_city("dhaka")
describe_city("khulna")
describe_city("tokyo", "japan")


# ==========================
# USER INPUT + DEFAULT FUNCTION
# ==========================

user_number = int(input("Enter a number: "))

power(user_number, 2)


# ==========================
# HOMEWORK
# ==========================

# 1. Write a function called make_shirt(size, text)
#    that prints the shirt size and message.
#    Call it once with positional arguments and once
#    with keyword arguments.

# 2. Modify make_shirt() so that:
#    - size defaults to "Large"
#    - text defaults to "I love Python"
#    Create:
#    - a large shirt with defaults
#    - a medium shirt with the default message
#    - a custom shirt with your own message

# 3. Write a function called describe_city(city, country)
#    with a default country value.
#    Call it for three different cities.

# 4. Write a function called rectangle_area(length, width=1)
#    that prints the area of a rectangle.
#    Call it:
#    - with one argument
#    - with two arguments

# 5. Write a function called introduce(name, city="Dhaka")
#    that prints:
#    "My name is Rishat and I live in Dhaka."
#    Call it with and without the city argument.

# 6. Challenge:
#    Write a function called calculator(number, power_value=2)
#    that prints number ** power_value.
#    Ask the user for a number and call the function.
