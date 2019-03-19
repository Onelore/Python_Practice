from python_carsh_course.ch09.car import Car
my_new_car = Car('benz', 's6000', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
