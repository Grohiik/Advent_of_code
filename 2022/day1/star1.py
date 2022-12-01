from input import input

input = input.split("\n\n")
input = [i.split("\n") for i in input]

input = [sum([int(j) for j in i]) for i in input]
#input = [sum(i) for i in input]

input.sort()
print("least amout", input[0])  # Least
print("most amount", input[-1]) # most