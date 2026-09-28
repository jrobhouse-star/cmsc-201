ice_cream_flavors = ["vanilla", "strawberry", "chocolate"]
toppings = ["caramel", "marshmallow", "gummi bears"]
for flavorsindex in range(len(ice_cream_flavors)) :
        if flavorsindex == 0 or flavorsindex == 2 :
            print(ice_cream_flavors[flavorsindex] + " is tasty with " + toppings[toppingsindex])
        elif flavorsindex == 1 :
            for toppingsindex in range(len(toppings)) :
                print("strawberry" + " is fine on it's own")