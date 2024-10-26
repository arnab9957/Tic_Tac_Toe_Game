
from tkinter import *
root = Tk()
root.geometry("400x600")
root.title("Tic Tac Toc")
root.resizable (0, 0)

frame1 = Frame(root)
frame1.pack()
titleLable = Label(frame1,  text = "Tic Tac Toc", font=("Arial", 35,  "bold"), bg = "yellow", fg = "blue", width = 15 )
titleLable.grid(row = 0, column = 0 )

optionFrame = Frame(root, bg = "gray")
optionFrame.pack()

frame2 = Frame(root)
frame2.pack()

board = {1:" ", 2:" ", 3:" ",
         4:" ", 5:" ", 6:" ",
         7:" ", 8:" ", 9:" " }

turn = "x"
game_end = False
mode = "singlePlayer"

def changeModeToSinglePlayer():
    global mode
    mode = "singlePlayer"
    aiButton["bg"] = "lightblue"
    multiButton["bg"] =  "lightgray"

def changeModeToMultiPlayer():
    global mode
    mode = "multiPlayer"
    multiButton["bg"] =  "lightblue"
    aiButton["bg"] = "lightgray"

def updateBoardForComputerMove():
    for key in board.keys():
         buttons[key-1]["text"] = board[key]

def checkForWin(player):
    if board[1] == board[2] == board[3] == player :
          return True
    elif board[4] == board[5] == board[6] == player :
          return True
    elif board[7] == board[8] == board[9] == player :
          return True
    elif board[1] == board[4] == board[7] == player :
          return True
    elif board[2] == board[5] == board[8] == player :
          return True
    elif board[3] == board[6] == board[9] == player :
          return True
    elif board[1] == board[5] == board[9] == player :
          return True
    elif board[3] == board[5] == board[7] == player :
          return True
    else:
         return False
     
def checkForDraw():
     for i in board.keys():
          if board[i] == " ":
                return False
     
     return True

def minimax(board, isMaximizing):
     if checkForWin("o"):
          return 1
     if checkForWin("x"):
          return -1
     if checkForDraw():
          return 0
     if isMaximizing:
         bestScore = -100
         for key in board.keys():
                if board[key] == " ":
                    board[key] = "o"
                    score = minimax(board, False) # minimax_Algorithem
                    board[key] = " "
                    if score > bestScore:
                            bestScore = score
         return bestScore                  
     else:
         bestScore = 100
         for key in board.keys():
                if board[key] == " ":
                    board[key] = "x"
                    score = minimax(board, True) # minimax_Algorithem
                    board[key] = " "
                    if score < bestScore:
                            bestScore = score
         return bestScore        

def playComputer():
    #  global minimax
     bestScore = -100
     bestMove = 0
     for key in board.keys():
          if board[key] == " ":
               board[key] = "o"
               score = minimax(board, False) # minimax_Algorithem
               board[key] = " "
               if score > bestScore:
                    bestScore = score
                    bestMove = key
     board[bestMove] = "o"
               
def play(event):
        global turn, game_end
        if game_end :
         return 
        button  = event.widget
        strbutton = str(button)
        clicked = strbutton[-1]
        
        if clicked == "n":
            clicked = 1
        else:
            clicked = int(clicked)
        

        if button["text"] == " " :

            if turn ==  "x":
                board[clicked] = turn 
                if checkForWin(turn):
                 winningDisplay = Label(frame1,text= f"{turn}, Wins the game!!", font = ("Arial", 30, "bold"), bg = "green", fg = "yellow", width = 15 )
                 winningDisplay.grid (row = 0, column = 0, columnspan = 3 )
                 game_end = True

                turn = "o"
                updateBoardForComputerMove()

                if mode == "singlePlayer":                      
                    playComputer()
                    if checkForWin(turn):
                        winningDisplay = Label(frame1,text= f"{turn}, Wins the game!!", font = ("Arial", 30, "bold"), bg = "green", fg = "yellow", width = 15 )
                        winningDisplay.grid (row = 0, column = 0, columnspan = 3 )
                        game_end = True

                    turn = "x"
                    updateBoardForComputerMove()

            else:
                board[clicked] = turn
                updateBoardForComputerMove() 
                if checkForWin(turn):
                    winningDisplay = Label(frame1,text= f"{turn}, Wins the game!!", font = ("Arial", 30, "bold"), bg = "green", fg = "yellow", width = 15)
                    winningDisplay.grid (row = 0, column = 0, columnspan = 3 )
                    game_end = True

                turn = "x"
                updateBoardForComputerMove()                 

            if checkForDraw() == True:
             draw = Label(frame1,text= " Game Draw !!", font = ("Arial", 30, "bold"), bg = "green", fg = "yellow", width = 18)
             draw.grid (row = 0, column = 0, columnspan = 3 )
            
def restartGame():
    global game_end
    game_end = False
    for button in buttons:
        button["text"] = " "
    for i in board.keys():
         board[i] = " "

    titleLable = Label(frame1,  text = "Tic Tac Toc", font=("Arial", 35,  "bold"), bg = "yellow", fg = "blue", width = 15 )
    titleLable.grid(row = 0, column = 0 )                  


aiButton = Button(optionFrame, text = "SingelPlayer", font = ("Arial", 15, "bold" ), height = 1, width = 15, bg = "gray", relief = RAISED, borderwidth = 5, command = changeModeToSinglePlayer)
aiButton.grid(row = 0, column = 0, columnspan = 1, sticky=NW)

multiButton = Button(optionFrame, text = "MultiPlayer", font = ("Arial", 15, "bold" ), height = 1, width = 15, bg = "gray", relief = RAISED, borderwidth = 5, command = changeModeToMultiPlayer)
multiButton.grid(row = 0, column = 1, columnspan = 1, sticky=NW)


button1 =  Button(frame2, text = " ", height = 2, width = 5, font = ("Arial", 30,  "bold"), bg = "red", fg = "blue", relief = RAISED, borderwidth = 5 )
button1.grid(row=0, column=0)
button1.bind("<Button-1>", play)

button2 = Button(frame2, text = " ", height = 2, width = 5, font =("Arial", 30,  "bold"), bg = "red", fg = "blue", relief = RAISED, borderwidth = 5 )
button2.grid(row=0, column=1)
button2.bind("<Button-1>", play)

button3 = Button(frame2, text = " ", height = 2, width = 5, font =("Arial", 30,  "bold"), bg = "red", fg = "blue", relief = RAISED, borderwidth = 5 )
button3.grid(row=0, column=2)
button3.bind("<Button-1>", play)

button4 = Button(frame2, text = " ", height = 2, width = 5, font =("Arial", 30,  "bold"), bg = "red", fg = "blue", relief = RAISED, borderwidth = 5 )
button4.grid(row=1, column=0)
button4.bind("<Button-1>", play)

button5 = Button(frame2, text = " ", height = 2, width = 5, font =("Arial", 30,  "bold"), bg = "red", fg = "blue", relief = RAISED, borderwidth = 5 )
button5.grid(row=1, column=1)
button5.bind("<Button-1>", play)

button6 = Button(frame2, text = " ", height = 2, width = 5, font =("Arial", 30,  "bold"), bg = "red", fg = "blue", relief = RAISED, borderwidth = 5 )
button6.grid(row=1, column=2)
button6.bind("<Button-1>", play)

button7 = Button(frame2, text = " ", height = 2, width = 5, font =("Arial", 30,  "bold"), bg = "red", fg = "blue", relief = RAISED, borderwidth = 5 )
button7.grid(row = 2, column=0)
button7.bind("<Button-1>", play)

button8 = Button(frame2, text = " ", height = 2, width = 5, font =("Arial", 30,  "bold"), bg = "red", fg = "blue", relief = RAISED, borderwidth = 5 )
button8.grid(row = 2, column=1)
button8.bind("<Button-1>", play)

button9 = Button(frame2, text = " ", height = 2, width = 5, font =("Arial", 30,  "bold"), bg = "red", fg = "blue", relief = RAISED, borderwidth = 5 )
button9.grid(row = 2, column=2)
button9.bind("<Button-1>", play)

restarButton = Button(frame2, text = "Restart Game ?", font = ("Arial", 30, "bold" ), height = 1, width = 16, bg = "yellow", relief = RAISED, borderwidth = 5, command = restartGame)
restarButton.grid(row = 4, column = 0, columnspan = 3)
# restarButton.bind("<Button-1>", restartGame)  # Don't working...

buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]



root.mainloop()