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
            
if __name__ == '__main__':
    print('this is the cars module')