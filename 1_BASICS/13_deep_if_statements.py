# ==========================
# SIMPLE if
# ==========================

age = 20

if age >= 18:
    print("You are an adult.")

print("Program finished.")


# ==========================
# if / else
# ==========================

age = 16

if age >= 18:
    print("You can vote.")

else:
    print("You are too young to vote.")


# ==========================
# if / elif / else
# ==========================

marks = 78

if marks >= 80:
    print("Grade A")

elif marks >= 60:
    print("Grade B")

else:
    print("Need Improvement")


# ==========================
# MULTIPLE elif
# ==========================

food = "pasta"

if food == "pizza":
    print("This is my favorite food!")

elif food == "pasta":
    print("This is my second favorite.")

elif food == "burger":
    print("This is my third favorite.")

elif food == "biryani":
    print("I also enjoy biryani.")

else:
    print("I haven't tried this food.")



# ==========================
# MULTIPLE INDEPENDENT if
# ==========================

favorite_fruits = [
    "apple",
    "banana",
    "mango"
]

if "apple" in favorite_fruits:
    print("I really like apples!")

if "banana" in favorite_fruits:
    print("I really like bananas!")

if "orange" in favorite_fruits:
    print("I really like oranges!")

if "mango" in favorite_fruits:
    print("I really like mangoes!")

if "grapes" in favorite_fruits:
    print("I really like grapes!")


# ==========================
# BLOCKS MUST STAY TOGETHER
# ==========================

age = 20

# ❌ Incorrect

if age >= 18:
    print("Adult")

print("Hello")      
# This ends the if statement.

else:
    print("Minor")

# The code above will produce an error because
# else must come immediately after the if block.

# Correct version:
age = 20

if age >= 18:
    print("Adult")

else:
    print("Minor")

print("Program Finished")



# ==========================
# HOMEWORK
# ==========================

# 1. Create a variable called 'score'.
#    Use a simple if statement to print
#    "Excellent!" if the score is greater than 90.

# 2. Create a variable called 'age'.
#    Use an if/else statement to print:
#    - "Eligible to vote" if age is 18 or older.
#    - "Not eligible to vote" otherwise.

# 3. Create a variable called 'marks'.
#    Use an if/elif/else chain to print:
#    - Grade A (80 or above)
#    - Grade B (60–79)
#    - Grade C (40–59)
#    - Fail (below 40)

# 4. Create a variable called 'day'.
#    Use multiple elif statements to print a different
#    message for:
#    - Monday
#    - Friday
#    - Saturday
#    - Sunday
#    - Any other day

# 5. Create a list of at least four favorite foods.
#    Write multiple independent if statements that check
#    whether specific foods are in the list.
#    If a food exists, print a message saying you like it.

# 6. Create a list of your favorite programming languages.
#    Use a for loop with an if/elif/else chain to print:
#    - a special message for your favorite language
#    - another message for your second favorite
#    - another message for your third favorite
#    - a default message for everything else

# 7. Challenge:
#    Create a variable called 'weather'.
#    Depending on its value ("sunny", "rainy",
#    "cloudy", or "snowy"), print an appropriate activity
#    using an if/elif/else chain.