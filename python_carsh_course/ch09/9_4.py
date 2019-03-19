class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Our restaurant's name is " + self.restaurant_name.title())
        print("The cuisine type is " + self.cuisine_type.title())

    @staticmethod
    def open_restaurant():
        print("We are opening! Welcome to eat")

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, new_num):
        self.number_served += new_num

    def read_number_served(self):
        print("we can serve " + str(self.number_served) + " people")


restaurant = Restaurant('supreme', 'china food')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(int(input("how many people do you think this restaurant can server? ")))
restaurant.increment_number_served(89)
restaurant.read_number_served()
