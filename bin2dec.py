"""
Jonathan House CMSC201
bin2dec
"""
bin2dec = str(input())
decimal = 0
for digit in bin2dec:
        decimal = (decimal * 2) + int(digit)
print(decimal)