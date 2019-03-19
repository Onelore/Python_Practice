pizza = {
    'crust': 'thick',
    'topping': ['mushroom', 'extra cheese'],
}
print("your ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings: ")
for topping in pizza['topping']:
    print("\t" + topping)
