# ==========================
# INHERITANCE
# ==========================

class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.__odometer = 0

    def print_car_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

    def get_odometer(self):
        return self.__odometer

    def set_odometer(self, mileage):
        if mileage < self.__odometer:
            print("You cannot roll back the odometer.")
        else:
            self.__odometer = mileage


# ElectricCar inherits everything from Car
class ElectricCar(Car):

    def __init__(self, brand, model, year):
        super().__init__(
            brand=brand,
            model=model,
            year=year
        )

        self.battery = Battery(90)

    def print_range(self):
        if self.battery.capacity == 90:
            print("This car can travel around 400 km.")

        elif self.battery.capacity == 100:
            print("This car can travel around 450 km.")


# A separate class for the battery
class Battery:

    def __init__(self, capacity):
        self.capacity = capacity

    def print_battery_details(self):
        print(f"Battery capacity: {self.capacity} kWh")

    def upgrade_battery(self):
        if self.capacity != 100:
            self.capacity = 100
            print("Battery upgraded to 100 kWh.")

        else:
            print("Battery is already upgraded.")


# ==========================
# USING THE CLASSES
# ==========================

tesla = ElectricCar(
    brand="Tesla",
    model="Model X",
    year=2017
)

# These methods come from Car
tesla.print_car_details()

tesla.set_odometer(200)

print(f"Odometer: {tesla.get_odometer()}")

# Battery belongs to the ElectricCar
tesla.battery.print_battery_details()

# Check the range before upgrading
tesla.print_range()

# Upgrade the battery
tesla.battery.upgrade_battery()

# Check the range after upgrading
tesla.battery.print_battery_details()
tesla.print_range()


# ==========================================================
# HOMEWORK
# ==========================================================

# 1. Ice Cream Stand
#
# Create a class called Restaurant with:
# - restaurant name
# - cuisine type
#
# Then create an IceCreamStand class that inherits
# from Restaurant.
#
# Add a flavors attribute containing a list of
# ice cream flavors.
#
# Add a method that displays all the available flavors.
#
# Create an IceCreamStand object and display its flavors.


# 2. Admin
#
# Create a User class with:
# - first name
# - last name
# - age
#
# Then create an Admin class that inherits from User.
#
# Add a privileges attribute containing a list such as:
# - "can add post"
# - "can delete post"
# - "can ban user"
#
# Add a method called show_privileges() that displays
# all of the administrator's privileges.
#
# Create an Admin object and call the method.


# 3. Privileges
#
# Create a separate Privileges class.
#
# The class should contain a privileges attribute
# that stores a list of privileges.
#
# Add a show_privileges() method to this class.
#
# Then modify the Admin class so that it contains
# a Privileges object instead of storing the list directly.
#
# Create an Admin object and display its privileges.


# 4. Battery Upgrade
#
# Modify the Battery class so that it has an
# upgrade_battery() method.
#
# If the battery capacity is not 100 kWh,
# change it to 100 kWh.
#
# Create an ElectricCar with a default battery.
#
# Check its range.
#
# Upgrade the battery.
#
# Check the range again and make sure the range
# has increased.