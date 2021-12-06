from input import *

input = input.split(",")
input = [int(i, base=10) for i in input]


for j in range(80):
    for i in range(len(input)):
        if input[i] == 0:
            input.append(8)
            input[i] = 6
        else:
            input[i] -= 1


print(len(input))
