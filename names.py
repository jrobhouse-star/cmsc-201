def sum_string_lengths(strings):
    for x in strings:
        total_length = 0
    for x in strings:
        total_length += len(x)
    return total_length
def get_names():
    names = []
    name = ""
    while name != "STOP":
        names.append(name)
        name = input()
        print("Enter a name, STOP to stop: ", name)

    return names
if __name__ == '__main__':
    kitties = ["Jules", "Stubby", "Flash"]
    print("Length of kitties strings is ", sum_string_lengths(kitties))
    print("Length of names you typed in is ", sum_string_lengths(get_names()))