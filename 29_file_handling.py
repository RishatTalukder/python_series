# ==========================
# READING A TEXT FILE
# ==========================

file_path = "Relatuve or Absolute path"


# Reading the entire file at once
with open(file_path) as file:
    contents = file.read()

print(contents)


# ==========================
# READING LINE BY LINE
# ==========================

with open(file_path) as file:

    for line in file:
        print(line.rstrip())


# ==========================
# STORING LINES IN A LIST
# ==========================

with open(file_path) as file:
    lines = file.readlines()


for line in lines:
    print(line.rstrip())


# ==========================
# REPLACING TEXT
# ==========================

for line in lines:

    line = line.replace("Python", "JavaScript")

    print(line.rstrip())


# ==========================================================
# HOMEWORK
# ==========================================================

# 1. Create a file called learning_python.txt.
#
#    Write several lines about things you have learned
#    about Python.
#
#    Read the file and print its contents three times:
#
#    - Read the entire file at once.
#    - Loop through the file object and print each line.
#    - Store the lines in a list and print them after
#      leaving the with block.


# 2. Using learning_python.txt, read each line and replace
#    the word "Python" with another programming language.
#
#    Print the modified lines without changing the
#    original file.