# ==========================
# CREATING A DICTIONARY
# ==========================

cat = {
    "color": "brown",
    "age": 3
}

print(cat)

# ==========================
# ACCESSING VALUES
# ==========================

print(cat["color"])
print(cat["age"])

# ==========================
# ADDING NEW DATA
# ==========================

cat["eye_color"] = "green"
cat["name"] = "Tom"

print(cat)

# ==========================
# UPDATING VALUES
# ==========================

cat["color"] = "orange"

print(cat)

# ==========================
# REMOVING DATA
# ==========================

del cat["age"]

print(cat)

# ==========================
# USING get()
# ==========================

print(cat.get("color"))

print(cat.get("age"))

# setting default return value
print(cat.get("age", "Age not found"))

# ==========================
# [] vs get()
# ==========================

# This would cause an error if "breed" doesn't exist.
# print(cat["breed"])

print(cat.get("breed"))

print(cat.get("breed", "Unknown"))

# ==========================
# HOMEWORK
# ==========================

# 1. Create a dictionary that stores information about yourself.
#    Include at least:
#    - name
#    - age
#    - city
#    - favorite language
#    Print each value individually.

# 2. Create a dictionary for your favorite movie,
#    book, or game.
#    Print the entire dictionary.

# 3. Add two new key-value pairs to one of your
#    dictionaries and print the updated dictionary.

# 4. Update one of the existing values in your
#    dictionary and print the result.

# 5. Remove one key-value pair using del.
#    Print the dictionary after removing it.

# 6. Use get() to access:
#    - an existing key
#    - a key that doesn't exist
#    - a missing key with a default value

# 7. Challenge:
#    Create a dictionary describing your computer,
#    laptop, or phone.
#    Include at least six pieces of information
#    (for example: brand, model, RAM, storage,
#    operating system, and color).
#    Print all the information.