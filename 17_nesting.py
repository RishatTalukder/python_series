# ==========================
# LIST OF DICTIONARIES
# ==========================

cat_1 = {
    "name": "Tom",
    "color": "Orange"
}

cat_2 = {
    "name": "Lucy",
    "color": "Black"
}

cat_3 = {
    "name": "Milo",
    "color": "Brown"
}

cats = [cat_1, cat_2, cat_3]

for cat in cats:
    print(
        f"{cat['name']} is {cat['color']}."
    )
    
# ==========================
# DICTIONARY OF LISTS
# ==========================

menu = {
    "Pizza": [
        "Cheese",
        "Mushrooms",
        "Olives"
    ],

    "Burger": [
        "Bun",
        "Beef",
        "Cheese"
    ]
}

for food in menu:

    print(food)

    for ingredient in menu[food]:
        print(f"    - {ingredient}")
        
# ==========================
# ACCESSING ONE ITEM
# ==========================

favorite = "Pizza"

print(f"Ingredients of {favorite}:")

for ingredient in menu[favorite]:
    print(ingredient)
    
# ==========================
# DICTIONARY OF DICTIONARIES
# ==========================

users = {

    "rishat": {
        "first_name": "Rishat",
        "last_name": "Talukder",
        "city": "Dhaka"
    },

    "tom": {
        "first_name": "Tom",
        "last_name": "Smith",
        "city": "London"
    }

}

# ==========================
# LOOPING THROUGH NESTED DICTIONARIES
# ==========================

for username, info in users.items():

    print(username)

    print(f"First Name : {info['first_name']}")
    print(f"Last Name  : {info['last_name']}")
    print(f"City       : {info['city']}")

    print()
    
# ==========================
# HOMEWORK
# ==========================

# 1. Create three dictionaries representing three different
#    books, movies, or games.
#    Store them inside a list.
#    Loop through the list and print all the information.

# 2. Create a dictionary where each key is a programming
#    language and each value is a list of topics you have
#    learned in that language.
#    Print every language along with its topics.

# 3. Create a dictionary of students.
#    Each student should have another dictionary containing:
#    - age
#    - city
#    - favorite subject
#    Print all information neatly.

# 4. Modify the previous program by adding one more student
#    and one more piece of information to every student.

# 5. Create a dictionary of your favorite games.
#    Each game should have:
#    - genre
#    - release year
#    - platform
#    Print all of the information using nested loops.

# 6. Challenge:
#    Create a classroom dictionary.
#
#    Each student should have:
#        - age
#        - favorite language
#        - marks
#
#    Print the information in this format:
#
#    Student: Rishat
#        Age: 25
#        Favorite Language: Python
#        Marks: 95
#
#    Student: Tommy
#        ...