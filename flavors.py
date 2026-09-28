flavors = ["vanilla", "strawberry", "chocolate"]
toppings = ["caramel", "marshmallow", "gummi bears"]
for flavor in flavors :
    if flavor ==  "strawberry":
        print("strawberry is fine on its own")
    else:
        for topping in toppings:
            print(flavor + " is tasty with" + topping)