class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


# my_car = Car('audi', 'a4', 2018)
# print(my_car.get_descriptive_name())
# my_car.update_odometer(89)
# my_car.read_odometer()
#
# my_car.increment_odometer(9)
# my_car.read_odometer()
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    # def describe_battery(self):
    #     print("this car has a " + str(self.battery_size) + "-kwh battery")

    @staticmethod
    def fill_gas_tank():
        print("this car doesn't need a gas tank")


class Battery():
    def __init__(self, battery_size=85):
        self.battery_size = battery_size

    def describe_battery(self):
        print("this car has a " + str(self.battery_size) + "-kwh battery")

    def get_range(self):
        if self.battery_size == 70:
            ranges = 240
        elif self.battery_size == 85:
            ranges = 270
        message = "this car can go approximately " + str(ranges)
        message += " miles on a full charge."
        print(message)


# my_tesla = ElectricCar('Tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
