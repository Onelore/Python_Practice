sandwich_orders = ['tuna', 'oar', 'sandy', 'hot', 'hot', 'hot']
print("sorry,The hot pizza sold out!")
finished_sandwich = []
while 'hot' in sandwich_orders:
    sandwich_orders.remove('hot')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("\nI made your " + current_sandwich + "sandwich!")
    finished_sandwich.append(current_sandwich)
print("\t")
print(finished_sandwich)

