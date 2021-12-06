from input import *

input = input.split(",")
input = [int(i, base=10) for i in input]

# making new array that is 9 long and has the number of fish that age on each point
fishy = [0]*9
for fish in input:
    fishy[fish] += 1


for i in range(256):
    fish = fishy[0]
    for j in range(1, len(fishy)):
        fishy[j-1] = fishy[j]

    fishy[-1] = fish
    fishy[6] += fish


sum = 0
for i in fishy:
    sum += i
print(sum)

