print("Are you a hero or a villain? ")
heroVill = input()
if heroVill == "villain":
    print("What is your name? ")
    villName = input()
    print(villName + " sounds pretty evil!")
if heroVill == "hero":
    print("How many people have you saved? ")
    saved = int(input())
    if saved <= 10:
        print("Go on more patrols!")
    elif saved > 10 and saved < 100:
        print("Sounds like you're making a difference!")
    elif saved >= 100:
        print("Wow, great job saving the city!")