"""
Jonathan House (CMSC201)
remover.py two inputs, input line 1 sentence, input line 2 letter to remove from line 1
"""
def remover(line, to_remove):
    # your code here
    s = input().lower()
    print(s[0:])
    t = s
    print(t)
    t = t[1:] + t[0:1]
    while s != t:
        t = t[1:] + t[0:1]
        print(t)
    return 

if __name__ == "__main__":
    # finish this code: put your while loop to read user input here
    sentence = input()
    while input() != "stop":
        letter_to_remove = input()
       
        # and your function call here!

        sentence = input()