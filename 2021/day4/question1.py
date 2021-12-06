from input import *

numbers = numbers.split(",")

boards = boards.split("\n\n")

for i in range(len(boards)):
    boards[i] = boards[i].split("\n")
    for jj in range(len(boards[i])):
        boards[i][jj] = boards[i][jj].split(" ")

bingo = False
board_number = 0
sum = 0

for currentnumber in numbers:
    for i in range(len(boards)):
        if bingo:
            break
        board_number = i
        for ii in range(len(boards[i])):
            if bingo:
                break
            for iii in range(len(boards[i][ii])):
                if bingo:
                    break
                if boards[i][ii][iii] == currentnumber:
                    boards[i][ii][iii] = None
                    
                    for row in boards[i]:
                        if bingo:
                            break
                        number_of_found = 0
                        for element in row:
                            if element == None:
                                number_of_found+=1
                                if number_of_found == 4:
                                    print("blub")
                                if number_of_found == 5:
                                    bingo = True
                                    break

                    for colum in range(len(boards[i])):
                        if bingo:
                            break
                        number_of_found = 0
                        for element in range(len(boards[i][0])):
                            if boards[i][element][colum] == None:
                                number_of_found += 1
                                if number_of_found == 4:
                                    print("blub")
                                if number_of_found == 5:
                                    bingo = True
                                    break


    if bingo:
        for row in boards[board_number]:
            for element in row:
                if element != None:
                    sum += int(element)
        sum *= int(currentnumber)
        break

print(sum)