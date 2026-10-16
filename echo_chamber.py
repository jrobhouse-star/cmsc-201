"""
Jonathan House CMSC201
echo_chamber, repeat back what user types until type done, not printing done
"""
output = ""
while True:
    echo = input()
    if echo == "done":
        break
    if output =="":
        output = echo
    else:
        output = output + "\n" + echo
print(output)