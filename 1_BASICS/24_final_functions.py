# ==========================
# IMPORTING FUNCTIONS
# ==========================

# Assume there is another file named hello.py
# containing a function called power().

from hello import power as exponent
import random


# ==========================
# WORKING WITH LISTS
# ==========================

numbers = list(range(1, 11))


def square_numbers(arr):

    for i in range(len(arr)):
        arr[i] = exponent(arr[i], 2)

    return arr


# Pass a copy so the original list is unchanged.
squared = square_numbers(numbers.copy())

print("Squared list :", squared)
print("Original list:", numbers)


# ==========================
# SHOW MESSAGES
# ==========================

messages = [
    "Hello",
    "How are you?",
    "Welcome to Python"
]


def show_messages(msgs):

    for msg in msgs:
        print(msg)


show_messages(messages)


# ==========================
# SEND MESSAGES
# ==========================

sent_messages = []


def send_messages(msgs, sent_list):

    while msgs:
        current = msgs.pop()

        print(f"Sending: {current}")

        sent_list.append(current)


# Use a copy to keep the original list unchanged.
send_messages(messages.copy(), sent_messages)

print("\nOriginal messages:", messages)
print("Sent messages    :", sent_messages)


# ==========================
# SANDWICHES (*args)
# ==========================

def make_sandwich(*items):

    print("\nSandwich order:")

    for item in items:
        print(f"- {item}")


make_sandwich("cheese")
make_sandwich("cheese", "tomato")
make_sandwich(
    "cheese",
    "tomato",
    "lettuce",
    "mayo"
)


# ==========================
# USER PROFILE (**kwargs)
# ==========================

def build_profile(first, last, **user_info):

    profile = {
        "first_name": first.title(),
        "last_name": last.title()
    }

    profile.update(user_info)

    return profile


my_profile = build_profile(
    "rishat",
    "talukder",
    age=25,
    city="Dhaka",
    profession="Teacher"
)

print("\nUser Profile:")
print(my_profile)


# ==========================
# CAR INFORMATION (**kwargs)
# ==========================

def make_car(manufacturer, model, **car_info):

    car = {
        "manufacturer": manufacturer.title(),
        "model": model.title()
    }

    car.update(car_info)

    return car


car = make_car(
    "subaru",
    "outback",
    color="blue",
    tow_package=True
)

print("\nCar Information:")
print(car)


# ==========================
# RANDOM EXAMPLE
# ==========================

random_number = random.randint(1, 100)

print(f"\nRandom number: {random_number}")


# ==========================
# IMPORT EXAMPLES
# ==========================

# import hello
# hello.power(2, 3)

# from hello import power
# power(2, 3)

# from hello import power as exponent
# exponent(2, 3)

# import hello as h
# h.power(2, 3)

# from hello import *
# power(2, 3)


# ==========================
# HOMEWORK
# ==========================

# 1. Create a list of text messages and write a function
#    show_messages() that prints each message.

# 2. Write a function send_messages() that moves messages
#    from one list to another while printing them.

# 3. Call send_messages() with a copy of the original list
#    and verify that the original list remains unchanged.

# 4. Write a function make_sandwich(*items) and call it
#    with different numbers of ingredients.

# 5. Write a function build_profile(first, last, **info)
#    and create a profile for yourself.

# 6. Write a function make_car(manufacturer, model, **info)
#    and create at least two car dictionaries.

# 7. Create a separate file containing a function and
#    practice importing it using:
#    - import module_name
#    - from module_name import function_name
#    - from module_name import function_name as fn
#    - import module_name as mn
#    - from module_name import *

# 8. Challenge:
#    Create a function called student_record(name, **details)
#    that returns a dictionary containing a student's name
#    and any additional information such as age, city,
#    marks, or favorite subject.
