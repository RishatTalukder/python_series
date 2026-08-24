# ==========================
# WRITING TO A FILE
# ==========================

# "w" = write mode
# If the file doesn't exist, Python creates it.
# If the file already exists, its old contents are replaced.

with open("text_folder/test.txt", "w") as file:

    file.write("This is the first line.\n")
    file.write("This is the second line.\n")


# ==========================
# APPENDING TO A FILE
# ==========================

# "a" = append mode
# New content is added to the end of the file.
# Existing contents are not deleted.

with open("text_folder/test.txt", "a") as file:

    file.write("This line was added later.\n")
    file.write("This is another new line.\n")


# ==========================
# READING THE FILE
# ==========================

with open("text_folder/test.txt", "r") as file:

    contents = file.read()

print(contents)


# ==========================
# READ AND WRITE MODE
# ==========================

# "r+" = read and write
# The file must already exist.
# You can read from and write to the same file.

with open("text_folder/test.txt", "r+") as file:

    contents = file.read()

    print(contents)

    file.write("\nThis line was added using r+ mode.")


# ==========================
# GETTING USER INPUT
# ==========================

name = input("Enter your name: ")

with open("text_folder/guest.txt", "w") as file:
    file.write(name)


# ==========================
# GUEST BOOK
# ==========================

print("Enter 'q' to quit.")

with open("text_folder/guest_book.txt", "a") as file:

    while True:

        name = input("Enter your name: ")

        if name == "q":
            break

        print(f"Welcome, {name.title()}!")

        file.write(f"{name}\n")


# ==========================
# PROGRAMMING POLL
# ==========================

print("Enter 'q' to stop the poll.")

with open("text_folder/programming_poll.txt", "a") as file:

    while True:

        reason = input(
            "Why do you like programming? "
        )

        if reason == "q":
            break

        file.write(f"{reason}\n")


# ==========================================================
# HOMEWORK
# ==========================================================

# 1. Guest
#
# Ask the user for their name and save it in a file
# called guest.txt.


# 2. Guest Book
#
# Create a while loop that asks users for their names.
#
# Print a greeting for each person and save their name
# in guest_book.txt.
#
# Make sure every name is written on a separate line.
#
# Let the user enter "q" to stop.


# 3. Programming Poll
#
# Create a while loop that asks users why they like
# programming.
#
# Save every response to programming_poll.txt.
#
# Each response should be on its own line.
#
# Let the user enter "q" to stop.