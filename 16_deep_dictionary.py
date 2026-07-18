# ==========================
# LOOPING THROUGH A DICTIONARY
# ==========================

student_marks = {
    "rishat": 32,
    "shagor": 69,
    "itvaya": 420
}

for student in student_marks:
    print(student)
    
# ==========================
# ACCESSING VALUES INSIDE A LOOP
# ==========================

student_marks = {
    "rishat": 32,
    "shagor": 69,
    "itvaya": 420
}

for student in student_marks:
    print(f"{student.title()} scored {student_marks[student]}")
    
# ==========================
# USING keys()
# ==========================

favorite_languages = {
    "rishat": "python",
    "shagor": "c++",
    "itvaya": "kotlin"
}

for name in favorite_languages.keys():
    print(name.title())
    
# ==========================
# USING values()
# ==========================

favorite_languages = {
    "rishat": "python",
    "shagor": "c++",
    "itvaya": "kotlin"
}

for language in favorite_languages.values():
    print(language.title())
    
# ==========================
# USING items()
# ==========================

favorite_languages = {
    "rishat": "python",
    "shagor": "c++",
    "itvaya": "kotlin"
}

for item in favorite_languages.items():
    print(item)
    
# ==========================
# TUPLE UNPACKING
# ==========================

person = ("Rishat", 25)

name, age = person

print(name)
print(age)

# ==========================
# items() WITH UNPACKING
# ==========================

favorite_languages = {
    "rishat": "python",
    "shagor": "c++",
    "itvaya": "kotlin"
}

for name, language in favorite_languages.items():
    print(
        f"{name.title()} likes {language.title()}"
    )
    
# ==========================
# HOMEWORK
# ==========================

# 1. Create a dictionary containing at least five
#    students and their marks.
#    Loop through the dictionary and print:
#    "<name> scored <marks>"

# 2. Create a dictionary of your favorite games,
#    movies, or programming languages.
#    Use keys() to print only the keys.

# 3. Using the same dictionary,
#    use values() to print only the values.

# 4. Use items() to print both keys and values
#    in a nicely formatted sentence.

# 5. Create a tuple containing:
#    - your name
#    - your age
#    Unpack the tuple into two variables and print them.

# 6. Create a dictionary containing at least
#    four countries and their capitals.
#    Use items() and tuple unpacking to print:
#    "The capital of Bangladesh is Dhaka."

# 7. Challenge:
#    Create a dictionary of at least five friends
#    and their favorite programming languages.
#
#    Print:
#    - all names using keys()
#    - all languages using values()
#    - complete sentences using items()