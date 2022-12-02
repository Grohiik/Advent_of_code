from input import input

input = input.split("\n")
input = [i.split(" ") for i in input]

output = 0

for them, me in input:
    if me == "X":
        output += 1
        if them == "A":
            output += 3
        elif them == "B":
            output += 0
        elif them == "C":
            output += 6
    elif me == "Y":
        output += 2
        if them == "A":
            output += 6
        elif them == "B":
            output += 3
        elif them == "C":
            output += 0
    elif me == "Z":
        output += 3
        if them == "A":
            output += 0
        elif them == "B":
            output += 6
        elif them == "C":
            output += 3


# This is disqusting
print(output)