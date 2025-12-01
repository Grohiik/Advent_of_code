from input import input

number = 0

rotation = 50
input = input.split("\n")

for row in input:
    way = row[0]
    amount = row[1:]

    if(way == "R"):
        rotation += int(amount)
    elif(way == "L"):
        rotation -= int(amount)

    rotation %= 100
    if(rotation == 0):
        number += 1

print(number)
