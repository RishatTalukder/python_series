# ==========================
# ENCAPSULATION
# ==========================

# Encapsulation means controlling how
# the data inside an object can be accessed
# or modified.


# ==========================
# PUBLIC ATTRIBUTES
# ==========================

class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer = 0

    def print_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


car = Car("Audi", "A4", 2021)

car.print_details()

# Public attributes can be accessed directly
print(car.odometer)

# They can also be changed directly
car.odometer = 100

print(car.odometer)

# ==========================
# PRIVATE ATTRIBUTES
# ==========================

class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

        # Double underscore makes this a private attribute
        self.__odometer = 0

    def print_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


car = Car("Audi", "A4", 2021)

car.print_details()

# This will not work:
# print(car.__odometer)

# ==========================
# GETTER METHOD
# ==========================

class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.__odometer = 0

    def get_odometer(self):
        return self.__odometer


car = Car("Audi", "A4", 2021)

print(car.get_odometer())

# ==========================
# SETTER METHOD
# ==========================

class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.__odometer = 0

    def get_odometer(self):
        return self.__odometer

    def set_odometer(self, mileage):

        if mileage < self.__odometer:
            print("You cannot roll back the odometer.")

        else:
            self.__odometer = mileage


car = Car("Audi", "A4", 2021)

print(car.get_odometer())

car.set_odometer(20)
print(car.get_odometer())

car.set_odometer(50)
print(car.get_odometer())

# This should not be allowed
car.set_odometer(10)

print(car.get_odometer())

# ==========================
# HOMEWORK
# ==========================

# 1. Create a class called BankAccount.
#
# Store:
#   - account holder's name
#   - account number
#   - balance
#
# Make the balance a private attribute.
#
# Create methods to:
#   - get the current balance
#   - deposit money
#   - withdraw money
#
# Make sure a user cannot withdraw more money
# than they currently have.


# 2. Create a class called Student.
#
# Store:
#   - name
#   - grade
#
# Make the grade a private attribute.
#
# Create:
#   - get_grade()
#   - set_grade()
#
# Do not allow the grade to be less than 0
# or greater than 100.


# 3. Create a class called GameCharacter.
#
# Store:
#   - name
#   - health
#
# Make health a private attribute.
#
# Create methods to:
#   - get_health()
#   - take_damage()
#   - heal()
#
# Make sure health can never become negative.


# 4. Challenge:
#
# Create a class called Product.
#
# Store:
#   - name
#   - price
#   - stock
#
# Make price and stock private.
#
# Create methods that allow you to:
#   - get the price
#   - change the price
#   - get the stock
#   - add stock
#   - sell an item
#
# Make sure:
#   - price cannot be negative
#   - stock cannot be negative
#   - you cannot sell more items than are available