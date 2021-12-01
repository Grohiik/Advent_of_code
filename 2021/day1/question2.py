from input import input

inputArray = input.split("\n")
inputint = [int(i, base=10) for i in inputArray]

newarray = []
newarray.append(inputint[0])
inputint.pop(0)

newarray.append(inputint[0])
newarray[0] += inputint[0]
inputint.pop(0)

newarray.append(inputint[0])
newarray[0] += inputint[0]
newarray[1] += inputint[0]
inputint.pop(0)

for i in inputint:
    newarray.append(i)
    newarray[-2] += i
    newarray[-3] += i


count = 0
before = 1000000
for i in newarray:
    if before < i:
        count += 1
    before = i

print(count)
