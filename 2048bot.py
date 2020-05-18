import random
import copy
import os

boardsize = int(input("enter the boardsize :"))
print(boardsize)
won = int(input("enter the number required for winning :"))
board = [[0 for i in range(boardsize)] for j in range(boardsize) ]

def display():
    largest = board[0][0]
    for row in board:
        for element in row:
            if element > largest:
                largest = element

    numspaces = len(str(largest))
    for row in board:
        currrow = " | "
        for element in row:
            if element == 0:
                currrow +=" " * numspaces + " | "
            else:
                currrow += (" " * (numspaces - len(str(element)))) + str(element) + " | "

        print(currrow)
    print()

display()

def mergeonerowl(row):
    for j in range(boardsize - 1):
        for i in range(boardsize - 1, 0, -1):
            if row[i-1] == 0:
                row[i-1] = row[i]
                row[i] = 0

    for i in range(boardsize - 1):
        if row[i] == row[i+1]:
            row[i] *= 2
            row[i+1] = 0

    for i in range(boardsize -1, 0, -1):
        if row[i-1] == 0:
            row[i - 1] == row[i]
            row[i] == 0
    return row

def merge_left(currentboard):
    for i in range(boardsize):
        currentboard[i] = mergeonerowl(currentboard[i])

    return currentboard

def reverse(row):

    new = []
    for i in range(boardsize - 1, -1, -1):
        new.append(row[i])
    return new

def merge_right(currentboard):
    for i in range(boardsize):
        currentboard[i] = reverse(currentboard[i])
        currentboard[i] = mergeonerowl(currentboard[i])
        currentboard[i] = reverse(currentboard[i])
    return currentboard

def transpose(currentboard):
    for j in range(boardsize):
        for i in range(j,boardsize):
            if not i==j :
                temp = currentboard[j][i]
                currentboard[j][i] = currentboard[i][j]
                currentboard[i][j] = temp
    return currentboard

def merge_up(currentboard):
    currentboard = transpose(currentboard)
    currentboard = merge_left(currentboard)
    currentboard = transpose(currentboard)

    return currentboard

def merge_down(currentboard):
    currentboard = transpose(currentboard)
    currentbord = merge_right(currentboard)
    currentboard = transpose(currentboard)

    return currentboard

def picknewvalue():
    if random.randint(1, 8) == 1:
        return 4
    else:
        return 2

def addnewvalue():
    rownum = random.randint(0 , boardsize -1)
    colnum = random.randint(0 , boardsize -1)

    while not board[rownum][colnum] == 0:
        rownum = random.randint(0,boardsize -1)
        colnum = random.randint(0,boardsize -1)

    board[rownum][colnum] = picknewvalue()

def won():
    for row in board:
        if 2048 in row:
            return True
    return False

def nomoves():
    tempboard1 = copy.deepcopy(board)
    tempboard2 = copy.deepcopy(board)

    tempboard1 = merge_down(tempboard1)
    if tempboard1 == tempboard2:
        tempboard1 = merge_up(tempboard1)
        if tempboard1 == tempboard2:
            tempboard1 = merge_left(tempboard1)
            if tempboard1 == tempboard2:
                tempboard1 = merge_right(tempboard1)
                if tempboard1 == tempboard2:
                    return True
    return False

board = []
for i in range(boardsize):
    row = []
    for j in range(boardsize):
        row.append(0)
    board.append(row)

numneeded = 2
while numneeded > 0 :
    rownum = random.randint(0, boardsize -1)
    colnum = random.randint(0,boardsize - 1)

    if board[rownum][colnum] == 0:
        board[rownum][colnum] = picknewvalue()
        numneeded -= 1

print("Welcome to 2048 bot!type w for up a for left d for right & s for down. Hope you enjoy")
display()

gameover = False
while not gameover:
    move = input("enter your move :")

    validinput = True

    tempboard = copy.deepcopy(board)

    if move =="d":
        board = merge_right(board)
    elif move =="w":
        board = merge_up(board)
    elif move =="a":
        board = merge_left(board)
    elif move =="s":
        board = merge_down(board)
    else:
        validinput = False

    if not validinput:
        print("appropraiate move,try again")

    else:
        if won():
            display()
            print("you won!")
            gameover = True

        addnewvalue()

        display()

        if nomoves():
            print("sorry!you have no more possible moves,you lost!")
            gameover = True





























