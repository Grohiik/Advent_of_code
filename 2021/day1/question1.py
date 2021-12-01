from input import input

inputArray = input.split("\n")
inputint = [int(i, base=10) for i in inputArray]

count = 0
before = 1000000
for i in inputint:
    if before < i:
        count += 1
    before = i

print(count)
