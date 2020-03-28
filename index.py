#create table
def create_table(N):
    t = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(0)
        t.append(row)
    return t
#display the table 
def display(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            print(table[i][j],end = " ")
        print()
    print()
    for i in range(len(table[0])):
        print(i+1,end = " ")
    print()

#get input from user 
def get_input(table,N, turn):
    instr = 'Input a slot player {0} from 1 to {1}: '.format(turn,N)
    while True:
        try:
            inter= int(input(instr))
        except ValueError:
            print('invalid input:', inter)
            continue
        if 0 > inter or inter > N:
            print('invalid input:', inter)
        elif table[0][inter-1] != 0:
            print('slot', inter, 'is full try again')
        else:
            return inter

#checks if the game is a tie 
def tie(table):
    for i in range(len(table[0])):
        if(table[0][i] == 0):
            return False
    return True




def check_row(t,i,j):
    return t[i][j] == t[i][j+1] == t[i][j+2] ==t[i][j+3] !=0

def check_col(t,i,j):
    return t[i][j] == t[i+1][j] == t[i+2][j] ==t[i+3][j] !=0

def check_diagul(t,i,j):
    return t[i][j] == t[i+1][j+1] == t[i+2][j+2] ==t[i+3][j+3] !=0

def check_diagll(t,i,j):
    return t[i][j] == t[i-1][j+1] == t[i-2][j+2] ==t[i-3][j+3] !=0

def check_diagur(t,i,j):
    return t[i][j] == t[i+1][j-1] == t[i+2][j-2] ==t[i+3][j-3] !=0

def check_diaglr(t,i,j):
    return t[i][j] == t[i-1][j-1] == t[i-2][j-2] ==t[i-3][j-3] !=0





def winner(table,N):
    for i in range(N):
        for j in range(N):
            if(j + 3 < N and check_row(table,i,j)):
                return True
            if(i + 3 < N and check_col(table,i,j) ):
                return True
            if (j + 3 < N and i + 3 < N and check_diagul(table,i,j) ):
                return True
            if (i - 3 < N and j + 3 < N and check_diagll(table,i,j) ):
                return True
            if (i + 3 < N and j - 3 < N and check_diagur(table,i,j) ):
                return True
            if (i - 3 < N and j - 3 < N and check_diaglr(table,i,j) ):
                return True


    return False



def rotate90Clockwise(table,N,k):
    for l in range(0,k):
        n= len(table[0])
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                temp = table[i][j]
                table[i][j] = table[n-1 - j][i]
                table[n-1 -j][i] = table[n- 1 - i][n -1 -j]
                table[n -1 -i][n -1 -j] = table[j][n - 1 - i]
                table[j][n - 1 - i] = temp
            for i in range(N):
                fall(table,N)

def fall(table,N):

    for i in range(N-1):
        for j in range(N):
            if table[i+1][j]== 0 :
                table[i+1][j]=table[i][j]
                table[i][j]=0
    
    display(table)

def playagain():
    print ("Do you want to play again\n?")
    x = input("Press Y or y to play again")
    if x == 'Y' or x== 'y':
        connect4()

def connect4():
    N = int(input('Enter the grid size (N): '))
    table = create_table(N)
    turn = "X"
    while(True):

            display(table)
            drop = (get_input(table,N, turn))-1
           
            for i in range((len(table)-1),-1,-1):
                if(table[i][drop] == 0):
                    table[i][drop] = turn
                    break
            k=int(input("How many times you wanna rotate?"))      
            rotate90Clockwise(table,N,k)
            if(winner(table,N)):
                print("Win",turn)

            if(winner(table,N)==True):
                playagain()
                break

            if(tie(table)):
                break

            if(turn == "X"):
                turn = "O"
            else:
                turn = "X"

    print(table)

connect4()
