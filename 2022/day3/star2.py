from input import input

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

input = input.split("\n")

blub = []
while (len(input) >= 3):
    blub.append([input.pop(0), input.pop(0), input.pop(0)])
    print(blub[-1])

input = blub
input = ["".join(set(word_1).intersection(word_2).intersection(word_3)) for (word_1, word_2, word_3) in input]
input = [alphabet.index(i)+1 for i in input]
output = sum(input)

print(output)