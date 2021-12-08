from input import *

input = input.split("\n")
for i in range(len(input)):
    input[i] = input[i].split("|")[1].split(" ")

sum = 0
for i in input:
    for j in i:
        if len(j) == 2 or len(j) == 4 or len(j) == 3 or len(j) == 7:
            sum+=1

print(sum)