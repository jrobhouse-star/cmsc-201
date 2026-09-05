bool(0) == False
bool(1) == True
sideWalk = float(input())
steps = float(input())
distance = sideWalk * steps
is_even = distance % 2 != 0
print(bool(is_even))