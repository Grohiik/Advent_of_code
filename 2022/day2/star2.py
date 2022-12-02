from input import input

input = input.split("\n")
input = [i.split(" ") for i in input]

output = 0

for them, me in input:
    if me == "X":
        output += 0
        if them == "A":
            output += 3
        elif them == "B":
            output += 1
        elif them == "C":
            output += 2
    elif me == "Y":
        output += 3
        if them == "A":
            output += 1
        elif them == "B":
            output += 2
        elif them == "C":
            output += 3
    elif me == "Z":
        output += 6
        if them == "A":
            output += 2
        elif them == "B":
            output += 3
        elif them == "C":
            output += 1


# This is disqusting
print(output)