from input import input

marker_length = 14

for i in range(marker_length, len(input)+1):
    if (len(set(input[i-marker_length:i])) == marker_length):
        print(i)
        break;