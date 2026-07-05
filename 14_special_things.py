# ==========================
# MEMBERSHIP OPERATORS
# ==========================

foods = [
    "pizza",
    "burger",
    "pasta",
    "biryani"
]

favorite = "pizza"

if favorite in foods:
    print(f"{favorite.title()} is in the list.")

if "sushi" not in foods:
    print("Sushi is not in the list.")

# ==========================
# USING "in" INSIDE A LOOP
# ==========================

foods = [
    "pizza",
    "burger",
    "pasta",
    "biryani"
]

favorite = "pizza"

for food in foods:

    if food == favorite:
        print(f"{food.title()} is my favorite!")

    else:
        print(f"{food.title()} is okay.")

# ==========================
# THE "is" OPERATOR
# ==========================

foods = [
    "pizza",
    "burger",
    "pasta"
]

new_foods = foods

if new_foods is foods:
    print("Both variables refer to the same list.")

else:
    print("They are different lists.")

# Changing one list changes the other
# because both variables point to the same object.

new_foods[0] = "Sushi"

print(foods)
print(new_foods)

# ==========================
# CREATING A REAL COPY
# ==========================

foods = [
    "pizza",
    "burger",
    "pasta"
]

copied_foods = foods.copy()

print(copied_foods is foods)
print(copied_foods == foods)


# ==   -> same values?

# is   -> same object?

# ==========================
# TRUTHY & FALSY VALUES
# ==========================

if "":
    print("Non-empty strings are Truthy.")

if 100:
    print("Non-zero numbers are Truthy.")

if [1, 2, 3]:
    print("Non-empty lists are Truthy.")

# ==========================
# FALSY VALUES
# ==========================

if "":
    print("You won't see this.")

else:
    print("Empty strings are Falsy.")

if []:
    print("You won't see this.")

else:
    print("Empty lists are Falsy.")

if 0:
    print("You won't see this.")

else:
    print("Zero is Falsy.")

if None:
    print("You won't see this.")

else:
    print("None is also Falsy.")

# Common Falsy values

False
0
0.0
""
''
[]
{}
set()
None

# Everything else is generally Truthy.


# ==========================
# HOMEWORK
# ==========================

# 1. Create a list of at least five favorite foods.
#    Check whether:
#    - your favorite food is in the list
#    - a food you don't like is not in the list
#    Print appropriate messages for both cases.

# 2. Create a list of programming languages.
#    Use a for loop and print a special message if the
#    language is your favorite.
#    Print a different message for all other languages.

# 3. Create two variables that reference the same list.
#    Use the 'is' operator to check whether they point
#    to the same object.

# 4. Create a real copy of a list using copy().
#    Compare the original and copied lists using:
#    - ==
#    - is
#    Observe the difference.

# 5. Modify the copied list.
#    Print both lists to verify that changing one
#    does not affect the other.

# 6. Experiment with Truthy values.
#    Write if statements using:
#    - a non-empty string
#    - a non-zero number
#    - a non-empty list
#    Observe which blocks execute.

# 7. Experiment with Falsy values.
#    Try:
#    - ""
#    - []
#    - {}
#    - 0
#    - None
#    See which if blocks execute and which don't.

# 8. Challenge:
#    Create a variable called username.
#    If it contains a value, print:
#    "Welcome back!"
#    Otherwise print:
#    "Please enter your username."

#    Do the same for a password variable.

