from input import input

input = input.split("\n\n")
input = [i.split("\n") for i in input]

input = [sum([int(j) for j in i]) for i in input]
#input = [sum(i) for i in input]

input.sort(reverse=True)
print("top three elves", sum(input[0:3])) # most