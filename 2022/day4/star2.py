from input import input

input = input.split("\n")
input = [i.split(",") for i in input]
input = [left.split("-")+(right.split("-")) for left, right in input]
input = [[int(i) for i in blub] for blub in input]

output = 0

for x1, x2, y1, y2 in input:
    if ((x1 >= y1 and x1 <= y2) or (x2 >= y1 and x2 <= y2) or ((x1 <= y1 and x2 >= y2) or (x1 >= y1 and x2 <= y2))):
        output += 1

print(output)