# ==========================
# IMPORTING CLASSES
# ==========================

from cars import Car


# Create an object from the imported class
audi = Car(
    brand="Audi",
    model="A4",
    year=2024
)

print(audi.get_odometer())

audi.set_odometer(100)

print(audi.get_odometer())

# ==========================================================
# HOMEWORK
# ==========================================================

# 1. Create a file called restaurant.py.
#    Put your Restaurant class inside it.
#
#    Create another Python file and import Restaurant.
#    Create a Restaurant object and call one of its methods.


# 2. Create a file containing the User, Admin,
#    and Privileges classes.
#
#    Create another Python file and import Admin.
#    Create an Admin object and display its privileges.


# 3. Split the classes into two modules.
#
#    Put User in one module.
#    Put Admin and Privileges in another module.
#
#    Import Admin into a third Python file.
#    Create an Admin object and display its privileges.