from input import input

inputArray = input.split("\n")
inputArray2d = []
for i in inputArray:
    inputArray2d.append(i.split(" "))
    inputArray2d[-1][1] = int(inputArray2d[-1][1])
# for j in range(len(inputArray2d)):
#   inputArray2d[j] = [int(i, base=10) for i in inputArray2d[1]]

position = 0
depth = 0
aim = 0
for i in inputArray2d:
    if i[0] == "forward":
        position += i[1]
        depth += i[1] * aim
    elif i[0] == "down":
        aim += i[1]
    elif i[0] == "up":
        aim -= i[1]

print(position * depth)
