key = str(input())
if len(key) % 3 != 0 or len(key) == 0:
    print("Invalid key! The authorities have been notified.")
else:
    is_valid = True
    for i in range(2, len(key), 3):
        digit = int(key[i])
    if digit % 2 != 0:
        is_valid = False
    if is_valid:
        print("Welcome! Booting the system!")
    else:
        print("Invalid key! The authorities have been notified.")