# ==========================
# BASIC while LOOP
# ==========================

count = 1

while count <= 5:
    print(count)
    count += 1

print("Loop finished.")

# ==========================
# FIXED NUMBER OF INPUTS
# ==========================

count = 0

while count < 3:
    name = input("Enter your name: ")
    print(f"Welcome, {name.title()}!")
    count += 1
    
# ==========================
# ACTIVE VARIABLE
# ==========================

active = True

while active:

    name = input("Enter your name (type 'quit' to stop): ")

    if name == "quit":
        active = False

    else:
        print(f"Welcome, {name.title()}!")

print("Program ended.")

# ==========================
# break
# ==========================

while True:

    name = input("Enter your name (type 'quit' to stop): ")

    if name == "quit":
        break

    print(f"Welcome, {name.title()}!")

print("Loop exited using break.")

# ==========================
# continue
# ==========================

count = 0

while count < 10:

    count += 1

    if count % 2 == 0:
        continue

    print(count)
    
# ==========================
# INFINITE LOOP
# ==========================

# WARNING: This loop never ends.

# while True:
#     print("This will run forever")

# ==========================
# HOMEWORK
# ==========================

# 1. Use a while loop to print numbers from 1 to 20.

# 2. Use a while loop to print even numbers from 2 to 20.

# 3. Ask the user for their name 5 times using a while loop.
#    Print a welcome message each time.

# 4. Create a loop that keeps asking for names until the
#    user types "quit".

# 5. Ask the user for numbers continuously.
#    Stop the loop when the user enters 0.

# 6. Create a simple calculator loop.
#    Ask for two numbers and print their sum.
#    Allow the user to quit by typing "quit".

# 7. Use continue to print only numbers divisible by 3
#    between 1 and 30.

# 8. Challenge:
#    Create a movie ticket program.
#
#    Ask the user for their age repeatedly.
#    Print:
#    - "Free ticket" if age < 3
#    - "Ticket price: $10" if age is between 3 and 12
#    - "Ticket price: $15" if age is greater than 12
#
#    Stop the program when the user types "quit".