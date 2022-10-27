def make_pizza(size,*toppings):
    print(f"making a {size} inch pizza with following toppings: ")
    for topping in toppings:
        print("\t - " + topping)

