from input import input

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

input = input.split("\n")
input = [[i[:int(len(i)/2)], i[int(len(i)/2):]] for i in input]
input = ["".join(set(word_1).intersection(word_2)) for (word_1, word_2) in input]
input = [alphabet.index(i)+1 for i in input]
output = sum(input)

print(output)