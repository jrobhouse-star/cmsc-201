s = input().lower()
print(s[0:])
t = s
print(t)
t = t[1:] + t[0:1]
while s != t:
    t = t[1:] + t[0:1]
    print(t)