def order_sandwich(*toppings):
    print("\nYou ordered following: ")
    for topping in toppings:
        print(topping)

order_sandwich('a', 'b', 'c')
order_sandwich('d', 'f')
