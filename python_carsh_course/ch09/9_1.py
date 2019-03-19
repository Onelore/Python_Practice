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


restaurant = Restaurant('supreme', 'china food')
restaurant.describe_restaurant()
restaurant.open_restaurant()
