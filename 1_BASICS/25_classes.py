# ==========================
# CREATING A CLASS
# ==========================

class Animal:

    def __init__(self, animal_type, name):
        self.animal_type = animal_type
        self.name = name

    def print_name(self):
        print(f"The animal's name is {self.name}")


# Creating an object
dog = Animal(animal_type="Dog", name="Tommy")

dog.print_name()

# ==========================
# CREATING MULTIPLE OBJECTS
# ==========================

dog = Animal("Dog", "Tommy")
cat = Animal("Cat", "Tiger")

dog.print_name()
cat.print_name()

# ==========================
# HOMEWORK
# ==========================

# 1. Create a class called Book.
#    The class should store:
#    - title
#    - author
#    - year
#
#    Add a method called describe_book() that prints
#    all of this information.
#
#    Create at least two Book objects and call the method
#    for each one.


# 2. Create a class called Car.
#    Store:
#    - brand
#    - model
#    - year
#
#    Add a method that prints a description of the car.
#    Create three different car objects and describe each one.


# 3. Create a class called Student.
#    Store:
#    - name
#    - age
#    - grade
#
#    Add a method called introduce() that prints a message
#    introducing the student.
#
#    Create at least three students and call introduce()
#    for each one.


# 4. Challenge:
#    Create a class called GameCharacter.
#
#    Store:
#    - name
#    - health
#    - level
#
#    Add two methods:
#    - show_stats()
#    - greet()
#
#    Create at least two characters and call both methods
#    for each character.