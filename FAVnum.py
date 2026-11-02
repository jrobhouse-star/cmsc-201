#create a dictionary of people and their fav num, there can be no more than one of each fav num, give a return if already taken
favnum = {}
while True:
    choice = input("What do you want to do? (add favorite number), print favorite numbers for <person>, or quit? ")
    
    if choice == "quit":
        print("Later friend")
        break

    elif choice == "add favorite number":
        person = input("enter the person's name: ").strip()
        num = int(input(f"Enter {person}'s favorite number: "))
        favnum[person] = num
        print(f"Added: {person}'s favorite number is {num}.")
        if num == favnum[person]:  
            print("That number has already been used.")
            
    elif choice.startswith("print "):
        person = choice.replace("print ", "").strip()
        if person in favnum:
            print(f"{person}'s favorite number is {favnum[person]}.")
        else:
            print(f"No favorite number found for {person}.")
    else:
        print("Needs to be exact dude, follow the promts")