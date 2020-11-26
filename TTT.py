x = ("_________")
x = list(x)
xwin = 0
owin = 0

def printmatrix():
    print("---------")
    print("| " + x[0] + " " + x[1] + " " + x[2] + " |")
    print("| " + x[3] + " " + x[4] + " " + x[5] + " |")
    print("| " + x[6] + " " + x[7] + " " + x[8] + " |")
    print("---------")

printmatrix()

test1 = 0

# inputs the coordinates, checks if they are integers and within parameters
def inputc(player):
    while True:
        global corx
        global cory
        corx, cory = input("Player " + player + " Please enter the coordinates: > ").split()
        try:
            corx = int(corx)
            cory = int(cory)
        except:
            print("You should enter numbers!")
            continue
        if corx <= 0 or corx >= 4 or cory <= 0 or cory >= 4:
            print("Coordinates should be from 1 to 3!")
            continue
        break

# inputs X into the coordinate
def inputx():
    global success
    success = False
    #test2 = False
    while success == False:
        if corx == 1 and cory == 3:
            if x[0] == "_" or x[0] == " ":
                x[0] = "X"
                printmatrix()
                success = True
                break
            else:
                print("This cell is occupied! Choose another one!")
                inputc()
        if corx == 2 and cory == 3:
            if x[1] == "_" or x[1] == " ":
                x[1] = "X"
                printmatrix()
                success = True
                break
            else:
                print("This cell is occupied! Choose another one!")
                inputc()
        if corx == 3 and cory == 3:
            if x[2] == "_" or x[2] == " ":
                x[2] = "X"
                printmatrix()
                success = True
                break
            else:
                print("This cell is occupied! Choose another one!")
                inputc()
        if corx == 1 and cory == 2:
            if x[3] == "_" or x[3] == " ":
                x[3] = "X"
                printmatrix()
                success = True
                break
            else:
                print("This cell is occupied! Choose another one!")
                inputc()
        if corx == 2 and cory == 2:
            if x[4] == "_" or x[4] == " ":
                x[4] = "X"
                printmatrix()
                success = True
                break
            else:
                print("This cell is occupied! Choose another one!")
                inputc()
        if corx == 3 and cory == 2:
            if x[5] == "_" or x[5] == " ":
                x[5] = "X"
                printmatrix()
                success = True
                break
            else:
                print("This cell is occupied! Choose another one!")
                inputc()
        if corx == 1 and cory == 1:
            if x[6] == "_" or x[6] == " ":
                x[6] = "X"
                printmatrix()
                success = True
                break
            else:
                print("This cell is occupied! Choose another one!")
                inputc()
        if corx == 2 and cory == 1:
            if x[7] == "_" or x[7] == " ":
                x[7] = "X"
                printmatrix()
                success = True
                break
            else:
                print("This cell is occupied! Choose another one!")
                inputc()
        if corx == 3 and cory == 1:
            if x[8] == "_" or x[8] == " ":
                x[8] = "X"
                printmatrix()
                success = True
                break
            else:
                print("This cell is occupied! Choose another one!")
                inputc()

# inputs O into the coordinate
def inputo():
    global success
    success = False
    #test2 = False
    while success == False:
        if corx == 1 and cory == 3:
            if x[0] == "_" or x[0] == " ":
                x[0] = "O"
                printmatrix()

                success = True
                break
            else:
                print("This cell is occupied! Choose another one!")
                inputc()
        if corx == 2 and cory == 3:
            if x[1] == "_" or x[1] == " ":
                x[1] = "O"
                printmatrix()
                success = True
                break
            else:
                print("This cell is occupied! Choose another one!")
                inputc()
        if corx == 3 and cory == 3:
            if x[2] == "_" or x[2] == " ":
                x[2] = "O"
                printmatrix()
                success = True
                break
            else:
                print("This cell is occupied! Choose another one!")
                inputc()
        if corx == 1 and cory == 2:
            if x[3] == "_" or x[3] == " ":
                x[3] = "O"
                printmatrix()
                success = True
                break
            else:
                print("This cell is occupied! Choose another one!")
                inputc()
        if corx == 2 and cory == 2:
            if x[4] == "_" or x[4] == " ":
                x[4] = "O"
                printmatrix()
                success = True
                break
            else:
                print("This cell is occupied! Choose another one!")
                inputc()
        if corx == 3 and cory == 2:
            if x[5] == "_" or x[5] == " ":
                x[5] = "O"
                printmatrix()
                success = True
                break
            else:
                print("This cell is occupied! Choose another one!")
                inputc()
        if corx == 1 and cory == 1:
            if x[6] == "_" or x[6] == " ":
                x[6] = "O"
                printmatrix()
                success = True
                break
            else:
                print("This cell is occupied! Choose another one!")
                inputc()
        if corx == 2 and cory == 1:
            if x[7] == "_" or x[7] == " ":
                x[7] = "O"
                printmatrix()
                success = True
                break
            else:
                print("This cell is occupied! Choose another one!")
                inputc()
        if corx == 3 and cory == 1:
            if x[8] == "_" or x[8] == " ":
                x[8] = "O"
                printmatrix()
                success = True
                break
            else:
                print("This cell is occupied! Choose another one!")
                inputc()

work = True

def wincheck():
  global owin
  global xwin
  if x[0]=="X":
      if x[3]=="X" and x[6]=="X":
          xwin +=1
      if x[1]=="X" and x[2]=="X":
          xwin +=1
      if x[4]=="X" and x[8]=="X":
          xwin +=1
  if x[4]=="X":
      if x[1]=="X" and x[7]=="X":
          xwin +=1
      if x[3]=="X" and x[5]=="X":
          xwin +=1
      if x[2]=="X" and x[6]=="X":
          xwin +=1
  if x[8]=="X":
      if x[2]=="X" and x[5]=="X":
          xwin +=1
      if x[6]=="X" and x[7]=="X":
          xwin +=1
  if x[0]=="O":
      if x[3]=="O" and x[6]=="O":
          owin +=1
      if x[1]=="O" and x[2]=="O":
          owin +=1
      if x[4]=="O" and x[8]=="O":
          owin +=1
  if x[4]=="O":
      if x[1]=="O" and x[7]=="O":
          owin +=1
      if x[3]=="O" and x[5]=="O":
          owin +=1
      if x[2]=="O" and x[6]=="O":
          owin +=1
  if x[8]=="O":
      if x[2]=="O" and x[5]=="O":
          owin +=1
      if x[6]=="O" and x[7]=="O":
          owin +=1
  #create a count for empty empty spaces to determine draw 0r tie
  y = x.count('_')
  #create a count for X and O do to determine win
  cx = x.count('X')
  cy = x.count('O')

  if cx>cy:
      diff = cx - cy
  elif cy>cx:
      diff = cy - cx
  else:
      diff=0

  output_found = False;

  if xwin==1 and owin==0:
      print("X wins")
      quit()

  if xwin==0 and owin==1:
      print("O wins")
      quit()

  if (xwin>=1 and owin>=1) or (diff>=2):
      print("Impossible")
      output_found = True;

 # if (output_found == False):
 #     if xwin==0 and owin==0 and y>=1:
 #         print("Game not finished")
 #         output_found = True;

  if (output_found == False):
      if xwin==0 and owin==0 and y==0:
          print("Draw")
          output_found = True;


while work:
  inputc("X")
  inputx()
  wincheck()
  inputc("O")
  inputo()
  wincheck()




