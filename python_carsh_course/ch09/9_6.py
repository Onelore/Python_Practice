class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Our restaurant's name is " + self.restaurant_name.title())
        print("The cuisine type is " + self.cuisine_type.title())

    @staticmethod
    def open_restaurant():
        print("We are opening! Welcome to eat")


class IceCreamStand(Restaurant):
    def __init__(self, ice_name, IceCream):
        super().__init__(ice_name, IceCream)
        self.flavors = ['sweet', 'hot', 'strawberry', 'apple']

my_ice = IceCreamStand('DQ', 'iceCream')
my_ice.describe_restaurant()
print(my_ice.flavors)
