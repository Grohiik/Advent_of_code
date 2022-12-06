from input import input

input = input.split("\n\n")

# parse begining stacks
matrix = input.pop(0)
matrix = matrix.split("\n")
matrix.pop()
matrix = [i.split(" ") for i in matrix]

transposed = list()
for i in range(len(matrix[-1])):
    row = list()
    for sublist in matrix:
        if sublist[i] == "":
        # 5 spaces where there isn't a box becomes 4 empty strings
            sublist.pop(i)
            sublist.pop(i)
            sublist.pop(i)
        row.append(sublist[i])
    transposed.append([i for i in row if i != ""])

matrix = transposed
matrix = [[j[1] for j in i] for i in matrix]

# parse moves
input = [i.split(" ") for i in input[0].split("\n")]
input = [[int(i[1]), int(i[3]), int(i[5])] for i in input]

# simulate
for (moves, from_stack, to_stack) in input:
    for i in range(moves):
        matrix[to_stack-1].insert(0, matrix[from_stack-1].pop(0))

output = ""
for i in matrix:
    output += i[0]
print(output)
