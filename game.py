
# Initialization of n*n grid
def create_grid():
    global n
    n = int(input("Enter grid size: "))

    global grids
    grids = []


    for i in range(0, n):
        grids.append([])

    for i in range(0, n):
        for j in range(0, n):
            grids[i].append(j)
            grids[i][j] = - 1
    grid_def()


# Displays the current state of the grid
def grid_def():
    grid = []

    for i in range(0, n):
        grid.append([])

    for i in range(0, n):
        for j in range(0, n):
            grid[i].append(j)
            grid[i][j] = "   "

    for i in range(0, n):
        for j in range(0, n):
            if grids[i][j] == 1:
                grid[i][j] = " X "
            elif grids[i][j] == 2:
                grid[i][j] = " O "

    e = "\n", "--- " * n, "\n"
    print(("".join(str(i) for i in e).join("|".join(str(x) for x in row) for row in grid)))


def user_def():
    global user
    if user < 2:
        user = 2
    else:
        user = 1


def slot_full_def():
    if grids[0][userInput - 1] != -1:
        complete_slot_full()
        print("Slot is full try again!!!")
        confirm_def()


def confirm_def():
    loop_2 = True
    while loop_2:
        try:
            global userInput
            userInput = int(input("\nInput a slot player " + str(user) + " from 1 to " + str(n) + ":\n"))

            if (n + 1) > userInput > 0:
                loop_2 = False
            else:
                print("Invalid integer value")
        except ValueError:
            print("Invalid Input")


def placement_def():
    counter = 0
    for i in range(n - 1, -1, -1):
        slot_full_def()
        if grids[i][userInput - 1] == -1:
            if user == 1:
                grids[i][userInput - 1] = 1
            elif user == 2:
                grids[i][userInput - 1] = 2
            grid_def()
            break


# prints who has won
def hasWon_def():
    print("Player " + str(user) + " has won!!!\nCongrats")
    play_again()


# checks if there is a winner
def check_Win():
    if user == 1:
        tile = 1
    elif user == 2:
        tile = 2

    # check horizontal spaces
    for y in range(n):
        for x in range(n - 3):
            if grids[x][y] == tile and grids[x + 1][y] == tile and grids[x + 2][y] == tile and grids[x + 3][y] == tile:
                hasWon_def()
                return False

    # check vertical spaces
    for x in range(n):
        for y in range(n - 3):
            if grids[x][y] == tile and grids[x][y + 1] == tile and grids[x][y + 2] == tile and grids[x][y + 3] == tile:
                hasWon_def()
                return False

    # check / diagonal spaces
    for x in range(n - 3):
        for y in range(3, n):
            if grids[x][y] == tile and grids[x + 1][y - 1] == tile and grids[x + 2][y - 2] == tile and grids[x + 3][y - 3] == tile:
                hasWon_def()
                return False

    # check \ diagonal spaces
    for x in range(n - 3):
        for y in range(n - 3):
            if grids[x][y] == tile and grids[x + 1][y + 1] == tile and grids[x + 2][y + 2] == tile and grids[x + 3][y + 3] == tile:
                hasWon_def()
                return False

    return True


def checkEmpty_def():
    global check
    for i in range(n - 1, -1, -1):
        for a in range(n - 1, -1, -1):
            check.append(grids[i][a])
    if -1 not in check:
        print("Full")


def checks_def():
    check_Win()
    checkEmpty_def()


def play_again():
    ch = input("Do you want to play again??(Y/N)")
    if ch.upper() == "YES" or ch.upper() == 'Y':
        menu()
    elif ch.upper() == "NO" or ch.upper() == 'N':
        print("Thank You!!!")
        exit()
    else:
        print("Invalid Input")
        play_again()


def complete_slot_full():
    count=0
    for i in range(0, n):
        if grids[userInput - 1][i] != -1:
            count=count+1
    if count == n:
        print("The complete slot is full,\n The game is a Tie.")
        play_again()
        exit()


def rotate90clockwise(k):
    for l in range(0,k):
        m = len(grids[0])
        for i in range(m // 2):
            for j in range(i, m - i - 1):
                temp = grids[i][j]
                grids[i][j] = grids[m - 1 - j][i]
                grids[m - 1 - j][i] = grids[m - 1 - i][m - 1 - j]
                grids[m - 1 - i][m - 1 - j] = grids[j][m - 1 - i]
                grids[j][m - 1 - i] = temp
    grid_def()
    fall()


def fall():
    print("After rotation: ")
    for k in range (n):
        for i in range(n-1):
            for j in range(n):
                if grids[i+1][j] == -1:
                    grids[i+1][j] = grids[i][j]
                    grids[i][j] = -1
    grid_def()


def play_c1():
    global user
    global check
    global loop
    create_grid()

    check = []

    user = 1

    loop = True

    while loop is True:
        loop = check_Win()
        if not loop:
            break
        confirm_def()
        placement_def()
        checks_def()
        user_def()

    grid_def()


def play_c2():
    global user
    global check
    global loop
    create_grid()

    check = []

    user = 1

    loop = True

    while loop:
        loop = check_Win()
        if not loop:
            break
        confirm_def()
        placement_def()
        checks_def()
        user_def()
        print("By how many times do you wan to rotate the grid")
        k = int(input())
        if k > 0:
            rotate90clockwise(k)


    grid_def()


def menu():
    print("n===MENU===")
    print("1.Play Without Rotation.")
    print("2.Play with Rotation.")
    cho=int(input("please enter 1 or 2 as per your choice."))
    if(cho==1):
        play_c1()
    elif (cho==2):
        play_c2()
    else:
        print("Invalid Input")
        menu()

menu()

close
