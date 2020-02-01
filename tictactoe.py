board=[[1,2,3],[4,5,6],[7,8,9]]
game=True
symbol='X'
turn=0
print"Welcome to TicTacToe"
while game:
    turn+=1
    if turn%2==0:
        symbol='X'
    else:
        symbol='O'
    for line in board:
        print line
    ask=input("Enter a position from 1 to 9: ")
    if ask==1:
        board[0][0]=symbol
    elif ask==2:
        board[0][1]=symbol
    elif ask==3:
        board[0][2]=symbol
    elif ask==4:
        board[1][0]=symbol
    elif ask==5:
        board[1][1]=symbol
    elif ask==6:
        board[1][2]=symbol
    elif ask==7:
        board[2][0]=symbol
    elif ask==8:
        board[2][1]=symbol
    elif ask==9:
        board[2][2]=symbol
    if board[0][0]==board[0][1]==board[0][2] or board[1][0]==board[1][1]==board[1][2] or board[2][0]==board[2][1]==board[2][2] or board [0][0]==board[1][0]==board[2][0] or board[0][1]==board[1][1]==board[2][1] or board[0][2]==board[1][2]==board[2][2] or board[0][0]==board[1][1]==board[2][2] or board[02]==board[1][1]==board[2][0]:
        print "%s is the winner"%(symbol)
        game=False
    if turn==9:
        print "Tied"
        game=False

print "Press any character to quit"
x=input()
