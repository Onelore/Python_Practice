def car_infomation(maufactor_name, car_name, **car_info):
    car = {'malefactor': maufactor_name, 'cars_name': car_name}
    for key, value in car_info.items():
        car[key] = value
    return car
cars = car_infomation('subaru', 'outback', color='blue', two_package=True)
print(cars)
