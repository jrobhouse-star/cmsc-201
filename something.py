shelf_one = ["apple", "raspberries", "several pounds of chocolate"]
print("These are the products we have: ")
index = 0
for item in cart_items:
	index += 1
	print(f"\t{index}. " + item)
keep_going = input("Would you like to see the next shelf? ")

if keep_going.lower() == "y":
	items_on_display = ["dragonfruit", "olive oil", "Deathkiller, destroyer of worlds"]
	print("Please choose an item: ")
	index = 0
	for item in cart_items:
		index += 1
		print(f"\t{index}. " + item)
	item_chosen = input("Item to add: ")