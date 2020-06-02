# Battleship
# by Katherine Mercer

import random


gridsize = 10
gridwidth = 3
ships = {'Aircraft Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
hitmark = "x"
missmark = "."
missmarkb = "o"


### PRINTING ###

def printgrid(grid):
    for i in range(len(grid)):
        if i == 0:
            print('  ',end='') # initial spacing
        for j in range(int((gridwidth-1)/2)+1):
            print(' ',end='') # centering
        print(chr(65+i),end='') # letter label
        for j in range(int((gridwidth-1)/2)):
            print(' ',end='') # centering
    print()
    printgridlinetop(2)
    print()
    for i in range(len(grid)):
        print(i,end=' ')
        for j in range(len(grid)):
            if type(grid[i][j]) is int: # grid has probability info
                if grid[i][j] >= 100:
                    print(f"\u2502{grid[i][j]}",end="")
                elif grid[i][j] >= 10:
                    print(f"\u2502 {grid[i][j]}",end="")
                else:
                    print(f"\u2502  {grid[i][j]}",end="")
            else:
                print("\u2502",end='') # separator bars
                print(f" {grid[i][j]} ",end='') # grid content
        print("\u2502")
        if i != (len(grid)-1):
            printgridlinemid(2)
            print()
    printgridlinebottom(2)
    print()

def printgrids(grid1, grid2, grid1name="", grid2name=""):
    # grid names
    if len(grid1name) > 1 or len(grid2name) > 1:
        centergrid(grid1name, grid1)
        print(" ",end="")
        centergrid(grid2name, grid2)
        

    print()
    # grid1 labels
    for i in range(len(grid1)):
        for j in range(int((gridwidth-1)/2)+1):
            print(" ",end="") # centering
        print(chr(65+i),end="") # letter label
        for j in range(int((gridwidth-1)/2)):
            print(" ",end="") # centering
    print("  ",end="")

    # grid2 labels
    for i in range(len(grid2)):
        for j in range(int((gridwidth-1)/2)+1):
            print(" ",end="") # centering
        print(chr(65+i),end="") # letter label
        for j in range(int((gridwidth-1)/2)):
            print(" ",end="") # centering
    
    print()
    printgridlinetop()
    print(" ",end="")
    printgridlinetop()
    print()
    for i in range(len(grid1)):
        for j in range(len(grid1)):
            if type(grid1[i][j]) is int: # grid has probability info
                if grid1[i][j] >= 100:
                    print(f"\u2502{grid1[i][j]}",end="")
                elif grid1[i][j] >= 10:
                    print(f"\u2502 {grid1[i][j]}",end="")
                else:
                    print(f"\u2502  {grid1[i][j]}",end="")
            else:
                print("\u2502",end="") # separator bars
                print(f" {grid1[i][j]} ",end="") # grid content
        print("\u2502",end="")
                
        print(i,end="")
        
        for j in range(len(grid2)):
            if type(grid2[i][j]) is int: # grid has probability info
                if grid2[i][j] >= 100:
                    print(f"\u2502{grid2[i][j]}",end="")
                elif grid2[i][j] >= 10:
                    print(f"\u2502 {grid2[i][j]}",end="")
                else:
                    print(f"\u2502  {grid2[i][j]}",end="")
            else:
                print("\u2502",end="") # separator bars
                print(f" {grid2[i][j]} ",end="") # grid content
        print("\u2502")
        if i != (len(grid1)-1):
            printgridlinemid()
            print(" ",end="")
            printgridlinemid()
            print()
    printgridlinebottom()
    print(" ",end="")
    printgridlinebottom()
    print()

def printshipgrids(ships1, grid1, ships2, grid2):
    shipdic = ["A","B","C","S","D"]
    for i in range(len(shipdic)):
        ships1[i] = True
        ships2[i] = True
    for x in range(gridsize):
        for y in range(gridsize):
            if grid1[y][x] == "A":
                ships1[0] = False
            if grid1[y][x] == "B":
                ships1[1] = False
            if grid1[y][x] == "C":
                ships1[2] = False
            if grid1[y][x] == "S":
                ships1[3] = False
            if grid1[y][x] == "D":
                ships1[4] = False
                
            if grid2[y][x] == "A":
                ships2[0] = False
            if grid2[y][x] == "B":
                ships2[1] = False
            if grid2[y][x] == "C":
                ships2[2] = False
            if grid2[y][x] == "S":
                ships2[3] = False
            if grid2[y][x] == "D":
                ships2[4] = False

    printgridlinetop(0,5)
    for i in range(int(((gridsize-len(shipdic))*gridwidth)*(4/3))+1):
        print(" ",end="")
    printgridlinetop(0,5)
    print()
    print("\u2502",end="")
    for i in range(len(shipdic)):
        print(shipdic[i]+" ",end="")
        if ships1[i]:
            print("\u25a1",end="")
        else:
            print("\u25a0",end="")
        print("\u2502",end="")

    for i in range(int(((gridsize-len(shipdic))*gridwidth)*(4/3))+1):
        print(" ",end="")
    
    print("\u2502",end="")
    for i in range(len(shipdic)):
        print(shipdic[i]+" ",end="")
        if ships2[i]:
            print("\u25a1",end="")
        else:
            print("\u25a0",end="")
        print("\u2502",end="")
    print()
    printgridlinebottom(0,5)
    for i in range(int(((gridsize-len(shipdic))*gridwidth)*(4/3))+1):
        print(" ",end="")
    printgridlinebottom(0,5)
        

def printline(width):
    for i in range(int(width)):
        print("\u2500", end="")

def printgridlinemid(spaces=0, cells=gridsize):
    for x in range(spaces):
        print(" ",end="")
    print("\u251c",end="")
    for i in range(cells):
        printline(gridwidth)
        if i == cells-1:
            print("\u2524",end="")
        else:
            print("\u253c",end="")

def printgridlinetop(spaces=0, cells=gridsize):
    for x in range(spaces):
        print(" ",end="")
    print("\u250c",end="")
    for i in range(cells):
        printline(gridwidth)
        if i == cells-1:
            print("\u2510",end="")
        else:
            print("\u252c",end="")

def printgridlinebottom(spaces=0, cells=gridsize):
    for x in range(spaces):
        print(" ",end="")
    print("\u2514",end="")
    for i in range(cells):
        printline(gridwidth)
        if i == cells-1:
            print("\u2518",end="")
        else:
            print("\u2534",end="")

def pubgen(grid):
    publicgrid = [[" " for i in range(gridsize)] for j in range(gridsize)]
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == missmark:
                publicgrid[y][x] = missmarkb            
            elif grid[y][x].islower():
                publicgrid[y][x] = hitmark
            else:
                publicgrid[y][x] = " "
    return publicgrid

###   ###   ###   ###   ###   ###   ###   ###   ###   ###

def hasintersection(grid, y, x, verbose=True):
    #print(f"checking intersection {x},{y}")
    if x >= gridsize or y >= gridsize or x < 0 or y < 0:
        if verbose:
            print(f"\tShip out of bounds! ({numtocoord(x)}{y})")
        return True
    elif grid[y][x]!=" ":
        if verbose:
            print(f"\tCell already occupied! ({numtocoord(x)}{y})")
        return True
    else:
        #print("\tpassed intersection test") # debug
        return False

def hasintersectionrange(grid, y1, y2, x1, x2, verbose=True):
    #print(f"checking intersection range ({x1},{y1}) - ({x2},{y2})") # debug
    i = y1
    while i <= y2:
        j = x1
        while j <= x2:
            #print(f"checking cell ({i},{j})") # debug
            if hasintersection(grid, i, j, verbose):
                return True
            #print("cell check complete") # debug
            j+=1
        i+=1
    return False

def placeship(grid, shipname, y, x, isvertical=False, verbose=True):
    if isvertical:
        if not hasintersectionrange(grid, y, y+ships[shipname]-1, x, x, verbose):
            #print(f"\t\tadding {shipname}")
            for i in range(ships[shipname]):
                grid[y+i][x]=shipname[0]
            return True
        else:
            return False
    else:
        if not hasintersectionrange(grid, y, y, x, x+ships[shipname]-1, verbose):
            for i in range(ships[shipname]):
                grid[y][x+i]=shipname[0]
            return True
        else:
            return False

def inputgridloc():
    x = -1
    y = -1
    while x < 0 or y < 0 or x > gridsize or y > gridsize:
        cell = []
        while len(cell) < 2:
            #cell = input(f"Which cell would you like to place the top or left side of your {shipname} ({ships[shipname]} tiles) in?\nFor example, B0\n>: ")
            cell = input(">: ")
            #print(f"cell len:{len(cell)}") # debug
            x = -1
            y = -1

            try:
                x = int(coordtonum(cell[0].upper())) # first char is letter
            except:
                break
            else:
                try:
                    y = int(cell[1]) # second char is number
                except:
                    break
    return (cell,x,y)

def inputship(grid, shipname):
    placed = False
    while not placed:
        x = -1
        y = -1
        isvertical = ""
        confirm = False

        while x < 0 or y < 0 or x > gridsize or y > gridsize:
            print(f"Which cell would you like to place the top or left side of your {shipname} ({ships[shipname]} tiles) in?\nFor example, B0")
            cell, x, y = inputgridloc()
            
            if len(cell) == 3:
                v = cell[2]
                if v == "y" or v == "n":
                    isvertical = v
                elif v == "v":
                    isvertical = "y"
                elif v == "h":
                    isvertical = "n"
        #print(f"cell {x},{y}")

        while isvertical != "y" and isvertical != "n":
            isvertical = input("Should the ship be vertical? (y/n)\n>: ")
        #print(isvertical)
        if isvertical == "y":
            isvertical = True
        else:
            isvertical = False

        tempgrid = [[" " for i in range(gridsize)] for j in range(gridsize)]
        for row in range(gridsize):
            for col in range(gridsize):
                tempgrid[row][col] = grid[row][col]
                
        if placeship(tempgrid, shipname, y, x, isvertical):
            print(shipname[0])
            for row in range(gridsize):
                for col in range(gridsize):
                    if tempgrid[row][col] == shipname[0]:
                        tempgrid[row][col] = "\u25cb"
            printgrid(tempgrid)
            #choice = input(f"Placing {shipname} at {numtocoord(x)}{y}, is this correct? (y/n)\n>: ")
            if len(cell) != 3:
                print(f"Placing {shipname} ",end="")
                if isvertical:
                    print("vertically",end="")
                else:
                    print("horizontally",end="")
                print(f" at {numtocoord(x)}{y}, is this correct? (y/n)")
                choice = input(">: ")
                    
                if choice == "y":
                    placed = placeship(grid, shipname, y, x, isvertical)
                else:
                    print("Placement cancelled")
            else:
                placed = placeship(grid, shipname, y, x, isvertical)

def playersetup(name, iscomp):
    grid = [[" " for i in range(gridsize)] for j in range(gridsize)]
    #print(name)
    if not iscomp:
        printgrid(grid)
    for x in ships:
        if iscomp:
            placerandom(grid,x)
        else:
            inputship(grid, x)
            printgrid(grid)
    return grid

def placerandom(grid, ship):
    placed = False
    while not placed:
        randx = random.randint(0,9)
        randy = random.randint(0,9)
        randv = random.randint(0,1)
        if randv == 0:
            randv = False
        else:
            randv = True
        placed = placeship(grid, ship, randx, randy, randv, False)

def gridanalyze(grid):
    probabilitygrid = [[0 for i in range(gridsize)] for j in range(gridsize)]
    for s in ships:
        for y in range(gridsize):
            for x in range(gridsize):
                #print(f"Checking {s} at {x},{y} vertically") # debug
                if not hasintersectionrange(grid, y, y+ships[s]-1, x, x, False):
                    for i in range(y, y+ships[s]):
                        probabilitygrid[i][x] += 1
                #print(f"Checking {s} at {x},{y} horizontally") # debug
                if not hasintersectionrange(grid, y, y, x, x+ships[s]-1, False):
                    for i in range(x, x+ships[s]):
                        probabilitygrid[y][i] += 1
                #print("Checking hit marks") # debug
                if grid[y][x] == hitmark:
                    for i in range(-5,5):
                        if (y+i) >= 0 and (y+i) < gridsize and grid[y][x] != 0:
                            probabilitygrid[y+i][x] += (10-abs(i))
                        if (x+i) >= 0 and (x+i) < gridsize and grid[y][x] != 0:
                            probabilitygrid[y][x+i] += (10-abs(i))
    for y in range(gridsize):
        for x in range(gridsize):
            if grid[y][x] == hitmark:
                probabilitygrid[y][x] = 0
            if grid[y][x] == missmarkb:
                probabilitygrid[y][x] = 0
    return probabilitygrid

def compmove(probabilitygrid):
    movx = -1
    movy = -1
    bignum = -1
    for y in range(gridsize):
        for x in range(gridsize):
            if probabilitygrid[y][x] > bignum:
                movx = x
                movy = y
                bignum = probabilitygrid[y][x]
    #print(f"Computer attacks {numtocoord(movx)}{movy}!") # debug
    #print(f"(attack value {bignum})") # debug
    return (movx,movy)

def numtocoord(x):
    return chr(65+x)

def coordtonum(x):
    #print(f"converting {x}...") # debug
    return ord(x)-65

def movecheck(x,y):
    return 0

def attack(grid, x, y):
    if x >= gridsize or y >= gridsize:
        return -1
    if grid[y][x].islower():
        return -1
    if grid[y][x] == " ":
        grid[y][x] = "."
        print("SPLASH!\n")
        return 0
    elif grid[y][x].islower() or grid[y][x] == ".":
        return -1
    else:
        grid[y][x] = grid[y][x].lower()
        print("KABOOM!\n")
        return 1

def inputattack():
    x = -1
    y = -1
    while x < 0 or y < 0 or x > gridsize or y > gridsize:
        cell = []
        while len(cell) < 2:
            print(f"Which cell would you like to attack?")
            cell, x, y = inputgridloc()
            #print(f"cell len:{len(cell)}") # debug
            x = -1
            y = -1

            try:
                x = int(coordtonum(cell[0].upper())) # first char is letter
            except:
                break
            else:
                try:
                    y = int(cell[1]) # second char is number
                except:
                    break
                
    return (x,y)

def wincheck():
    p1 = 0
    p2 = 0
    for y in range(gridsize):
        for x in range(gridsize):
            if gridp1[y][x].isupper():
                p1 += 1
            if gridp2[y][x].isupper():
                p2 += 1
    if p1 == 0:
        return 2
    if p2 == 0:
        return 1
    return 0

def printcenter(size):
    for i in range(size):
        print(" ",end="")

def centergrid(msg, grid):
    center(msg, int(len(grid)*gridwidth*(4/3)))

def center(msg, width=80):
    odd = False
    f_half = (width-len(msg))/2
    if f_half != f_half+0.5:
        odd = True
    half = int(f_half)
    printcenter(half)
    if odd:
        print(" ",end="")
    print(msg,end="")
    printcenter(half)
                

#=============================================

gridp1 = [[" " for i in range(gridsize)] for j in range(gridsize)]
gridp2 = [[" " for i in range(gridsize)] for j in range(gridsize)]
shipsp1 = [False,False,False,False,False]
shipsp2 = [False,False,False,False,False]
compmoves = [[""]]

probabilitygrid2 = [[0 for i in range(gridsize)] for j in range(gridsize)]

win = 0
playercount = ""

spc = ""
for i in range(int((80-61)/2)):
    spc += " "
print(f"""
{spc}______  ___ _____ _____ _      _____ _____ _   _ ___________ 
{spc}| ___ \/ _ \_   _|_   _| |    |  ___/  ___| | | |_   _| ___ \\
{spc}| |_/ / /_\ \| |   | | | |    | |__ \ `--.| |_| | | | | |_/ /
{spc}| ___ \  _  || |   | | | |    |  __| `--. \  _  | | | |  __/ 
{spc}| |_/ / | | || |   | | | |____| |___/\__/ / | | |_| |_| |    
{spc}\____/\_| |_/\_/   \_/ \_____/\____/\____/\_| |_/\___/\_|    
{spc}=============================================================\n""")

msg = "Welcome to Battleship!"
center(msg)

while True:
    print("\n")

    ### number of players
    print("How many players are there? You can have a minimum of 0 and a maximum of 2.")
    while True:
        playercount = input(">: ")
        try:
            playercount = int(playercount)
        except ValueError:
            print("Please enter a number")
            continue

        if not (0 <= playercount <= 2):
            print("Please enter a number between 0 and 2 (inclusive)")
        else:
            break

    ### names
    ##  player 1
    p1name = input("Enter Player 1's name (or press enter for no name)\n>: ")
    try:
        p1name += ""
    except ValueError:
        p1name = ""
        continue
    if p1name == "":
        p1name = "Player 1"

    ##  player 2
    p2name = input("Enter Player 2's name (or press enter for no name)\n>: ")
    try:
        p2name += ""
    except ValueError:
        p2name = ""
        continue
    if p2name == "":
        p2name = "Player 2"

    ### determine autogen
    # 0p
    if playercount == 0:
        p1auto = True
        p2auto = True
    # 1p
    if playercount > 0:
        while True:
            p1auto = input(f"{p1name}, would you like to start with a random board? (y/n)\n>: ")
            if p1auto == "y":
                p1auto = True
                break
            elif p1auto == "n":
                p1auto = False
                break
    # 2p
    if playercount == 2:
        while True:
            p2auto = input(f"{p2name}, would you like to start with a random board? (y/n)\n>: ")
            if p2auto == "y":
                p2auto = True
                break
            elif p2auto == "n":
                p2auto = False
                break
    else:
        p2auto = True

    ### board setup
    gridp1 = playersetup(p1name, p1auto)
    gridp2 = playersetup(p2name, p2auto)

    ### play
    turns = 0
    atkresult = -1
    atkx = 0
    atky = 0
    while True:
        turns += 1

        # P1 delay
        if playercount > 0:
            for i in range(32):
                print()
            if atkresult >= 0:
                #print(f"\t{atkresult}") # debug
                if atkresult == 0:
                    atkresult = "missed"
                else:
                    atkresult = "hit"
                print(f"{p2name} {atkresult} at {numtocoord(atkx)}{atky}")
            input(f"Press enter when ready, {p1name}")
            for i in range(32):
                print()
        atkresult = -1
                
        # P1 move
        if playercount > 0:
            printgrids(gridp1, pubgen(gridp2), p1name, p2name) # display grids
        else:
            printgrid(gridp1)
        printshipgrids(shipsp1, gridp1, shipsp2, gridp2) # remaining ships
        print()
        printline(gridsize*gridwidth*(4/3))
        print(f"{p1name}'s turn")
        valid = False
        while not valid:
            if playercount > 0:
                atkx, atky = inputattack() # input player attack
            else:
                probabilitygrid1 = gridanalyze(pubgen(gridp2)) # calc probabilities
                atkx, atky = compmove(probabilitygrid1) # determine next move
            valid = attack(gridp2, atkx, atky)
            if valid >= 0:
                atkresult = valid
                valid = True
            else:
                valid = False
                print("Try again")
        win = wincheck()
        if win > 0: # end game on win
            break

        # P2 delay
        if playercount == 2:
            for i in range(32):
                print()
            if atkresult >= 0:
                #print(f"\t{atkresult}") # debug
                if atkresult == 0:
                    atkresult = "missed"
                else:
                    atkresult = "hit"
                print(f"{p1name} {atkresult} at {numtocoord(atkx)}{atky}")
            input(f"Press enter when ready, {p2name}")
            for i in range(32):
                print()
        atkresult = -1

        # P2 move
        if playercount == 2:
            printgrids(gridp2, pubgen(gridp1), p2name, p1name) # display grids
        else:
            printgrid(gridp2)
        printshipgrids(shipsp2, gridp2, shipsp1, gridp1) # remaining ships
        print()
        printline(gridsize*gridwidth*(4/3))
        print(f"{p2name}'s turn")
        valid = False
        while not valid:
            if playercount == 2:
                atkx, atky = inputattack() # input player attack
            else:
                probabilitygrid2 = gridanalyze(pubgen(gridp1)) # calc probabilities
                #printgrids(gridp1, probabilitygrid2) # debug
                atkx, atky = compmove(probabilitygrid2) # determine next move
            valid = attack(gridp1, atkx, atky)
            if valid >= 0:
                atkresult = valid
                valid = True
            else:
                valid = False
                print("Try again")
        win = wincheck()
        if win > 0: # end game on win
            break


    ### display winner
    if win == 1:
        winner = p1name
    else:
        winner = p2name

    printline(gridsize*gridwidth*(4/3))
    print(f"{winner} wins!")
    turnsmsg = "Total moves: "+str(turns)
    center(turnsmsg)
    print()


    printgrids(gridp1, gridp2, p1name, p2name)
    printshipgrids(shipsp1, gridp1, shipsp2, gridp2)
    print()
    #print("\n\t\t\t",end="")
    #print(f"{len(compmoves)} moves")
    """
    print("List of moves\nMOVE\tRESULT")
    for x in range(len(compmoves)):
        for y in range(len(compmoves[x])):
            print(compmoves[x][y],end="")
        print()
    """
    
    center("Would you like to play again? (y/n)")
    print()
    while True:
        playagain = input(">: ")
        if playagain == "n":
            playagain = False
            break
        elif playagain == "y":
            playagain = True
            break
    
    if not playagain:
        break
    else:
        center("Starting new game...")
