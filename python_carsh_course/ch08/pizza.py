def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + " pizza with the following toppings: ")
    for topping in toppings:
        print("\t" + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')
