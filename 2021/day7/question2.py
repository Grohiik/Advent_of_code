from input import *

input = input.split(",")
input = [int(i, base=10) for i in input]

crabship = [0] * 2000
for crab in input:
    crabship[crab] += 1


lowest_sum = 9999999999999999999999999999999999999999999999999999999999
for i in range(len(crabship)):
    current_sum = 0
    for currentvalue in range(len(crabship)):
        n = abs(currentvalue - i)
        current_sum += crabship[currentvalue] * (n * (n + 1) // 2)
    if current_sum < lowest_sum:
        lowest_sum = current_sum

print(lowest_sum)
