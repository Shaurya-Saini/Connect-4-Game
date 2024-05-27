import os

#Function for printing the board
def print_board(board):
    os.system("cls")
    for lis in board:
        str1=''
        str2=''
        for i in lis:
            str1=str1+f'| {i} '
            str2=str2+'+---'
        str1=str1+'|'
        str2=str2+'+'
        print(str1)
        print(str2)
    print("  1   2   3   4   5   6   7   ---- COLUMN NUMBERS\n")

#Function for accepting, validating and applying user input
def player01(board):
    inp = input('Player 1 enter the coloumn number form 1 to 7 = ')
    while inp.isdigit() == False:
        print('Wrong input')
        inp = input('Player 1 enter the coloumn number form 1 to 7 = ')
    colmn=int(inp)
    sign=0
    if colmn not in [1,2,3,4,5,6,7]:
        print('Wrong input')
        return player01(board)
    else:
        colmn-=1
        for lis in reversed(board):
            if lis[colmn]==' ':
                lis[colmn]='X'
                break
            else:
                sign+=1
                pass
        if sign==6:
            print('Wrong input')
            return player01(board)
        return board
def player02(board):
    colmn=int(input('Player 2 enter the coloumn number form 1 to 7 = '))
    sign=0
    if colmn not in [1,2,3,4,5,6,7]:
        print('Wrong input')
        return player02(board)
    else:
        colmn-=1
        for lis in reversed(board):
            if lis[colmn]==' ':
                lis[colmn]='O'
                break
            else:
                sign+=1
                pass
        if sign==6:
            print('Wrong input')
            return player02(board)
        return board

#Checking the winner
def check_winner(board):
    
    #Checking horizontally
    for row in board:
        num=0
        while num+4<=len(row):
            if row[num:num+4]==['X','X','X','X']:
                return 'Player 01 is the Winner'
            elif row[num:num+4]==['O','O','O','O']:
                return 'Player 02 is the Winner'
            num+=1
    
    #Checking vertically
    for colmn in range(0,7):
        row=0
        colmn_list=[]
        while row<=5:
            colmn_list.append(board[row][colmn])
            row+=1
        num=0
        while num+4<=len(colmn_list):
            if colmn_list[num:num+4]==['X','X','X','X']:
                return 'Player 01 is the Winner'
            elif colmn_list[num:num+4]==['O','O','O','O']:
                return 'Player 02 is the Winner'
            num+=1

    #Checking diagionally
    for row in range(4,6):
        for col in range(0,4):
            if board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3] == 'X':
                return 'Player 01 is the Winner'
            elif board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3] == 'O':
                return 'Player 02 is the Winner'
            if board[row][col+3] == board[row-1][col+2] == board[row-2][col+1] == board[row-3][col] == 'X':
                return 'Player 01 is the Winner'
            elif board[row][col+3] == board[row-1][col+2] == board[row-2][col+1] == board[row-3][col] == 'O':
                return 'Player 02 is the Winner'


lis1=[' ',' ',' ',' ',' ',' ',' ']
lis2=[' ',' ',' ',' ',' ',' ',' ']
lis3=[' ',' ',' ',' ',' ',' ',' ']
lis4=[' ',' ',' ',' ',' ',' ',' ']
lis5=[' ',' ',' ',' ',' ',' ',' ']
lis6=[' ',' ',' ',' ',' ',' ',' ']
board=[lis1,lis2,lis3,lis4,lis5,lis6]
print_board(board)
print('THE GAME BEGINS')

turn=0
while True:
    player01(board)
    print_board(board)
    if check_winner(board)=='Player 01 is the Winner':
        print(check_winner(board))
        break
    elif check_winner(board)=='Player 02 is the Winner':
        print(check_winner(board))
        break
    turn+=1
    if turn==42:
        break
    player02(board)
    print_board(board)
    if check_winner(board)=='Player 02 is the Winner':
        print(check_winner(board))
        break
    elif check_winner(board)=='Player 02 is the Winner':
        print(check_winner(board))
        break
    turn+=1
    if turn==42:
        print('THE GAME IS A DRAW')
        break
print(check_winner(board),'!')
print(check_winner(board),'!')
print(check_winner(board),'!')