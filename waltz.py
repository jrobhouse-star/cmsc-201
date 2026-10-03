steps = int(input())
waltz_1 = ""
for x in range(steps):
    if x > 5:
        waltz_1 = waltz_1 + str((x % 6) + 1)
    else:
        waltz_1 = waltz_1 + str(1 + x)
print(waltz_1)