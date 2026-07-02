# ==========================
# COMPARISON OPERATORS
# ==========================

age = 18
score = 85
username = "ITVAYA"

print(age == 18)          # True
print(age != 18)          # False

print(score > 80)         # True
print(score < 90)         # True

print(score >= 85)        # True
print(score <= 70)        # False

print(username.lower() == "itvaya")


# ==========================
# LOGICAL OPERATORS
# ==========================

age = 20
has_id = True

# and -> both conditions must be True
print(age >= 18 and has_id)

# or -> at least one condition must be True
print(age < 18 or has_id)

# not -> reverses a boolean value
print(not has_id)


# ==========================
# IF / ELSE
# ==========================

age = 16

if age >= 18:
    print("You can vote.")

else:
    print("You are too young to vote.")

# ==========================
# USING if INSIDE A LOOP
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
# HOMEWORK
# ==========================

# 1. Create at least 10 comparison expressions.
#    Make sure:
#    - at least 5 evaluate to True
#    - at least 5 evaluate to False
#    Print the result of each expression.

# 2. Create a string variable and practice:
#    - ==
#    - !=
#    - lower()
#    Compare it with different strings and observe the results.

# 3. Create two number variables.
#    Test all comparison operators:
#    - ==
#    - !=
#    - >
#    - <
#    - >=
#    - <=

# 4. Create two boolean variables.
#    Practice using:
#    - and
#    - or
#    - not
#    Print the result of each expression.

# 5. Create a list of at least five foods.
#    Check whether:
#    - your favorite food is in the list
#    - another food is not in the list
#    Print suitable messages.

# 6. Create a variable called age.
#    Use an if/else statement to print:
#    - "Adult" if age is 18 or older.
#    - "Minor" otherwise.

# 7. Create a list of your favorite games or programming languages.
#    Use a for loop with an if statement.
#    Print a special message for your favorite item and
#    a different message for all other items.

# 8. Challenge:
#    Create a simple login checker.
#    Store:
#    - username
#    - password
#
#    If BOTH are correct, print:
#    "Login Successful"
#
#    Otherwise print:
#    "Invalid username or password."