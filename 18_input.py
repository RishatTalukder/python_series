# ==========================
# BASIC INPUT
# ==========================

name = input("Enter your name: ")

print(f"Hello, {name.title()}!")

# ==========================
# CONVERTING TO INTEGER
# ==========================

age = input("Enter your age: ")

age = int(age)

print(age)
print(type(age))

# ==========================
# CONVERTING TO FLOAT
# ==========================

height = input("Enter your height in meters: ")

height = float(height)

print(height)
print(type(height))

# ==========================
# INPUT WITH if / else
# ==========================

age = int(input("Enter your age: "))

if age >= 18:
    print("Access granted.")

else:
    print("Access denied.")
    
# ==========================
# EVEN OR ODD
# ==========================

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")

else:
    print("Odd")
    
# ==========================
# HOMEWORK
# ==========================

# 1. Ask the user for their name and print a greeting.

# 2. Ask the user for their age.
#    Print whether they are an adult (18 or older)
#    or a minor.

# 3. Ask the user for a number.
#    Print whether the number is even or odd.

# 4. Ask the user for a number.
#    Print whether the number is positive,
#    negative, or zero.

# 5. Ask the user for two numbers.
#    Print:
#    - addition
#    - subtraction
#    - multiplication
#    - division

# 6. Ask the user for a number.
#    Print whether it is a multiple of 5.

# 7. Challenge:
#    Ask the user for their exam marks.
#
#    Print:
#    - "A" for 80 or above
#    - "B" for 60-79
#    - "C" for 40-59
#    - "Fail" below 40