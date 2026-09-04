print("What was the original price?")
originalPrice = float(input())
print("What is the new price?")
newPrice = float(input())
priceChange = (newPrice - originalPrice) / originalPrice * 100
print("Price changed by " + str(round(priceChange)) + "%")