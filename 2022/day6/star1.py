from input import input

for i in range(4, len(input)+1):
    if (len(set(input[i-4:i])) == 4):
        print(i)
        break;
