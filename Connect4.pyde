
#Welcome to Connect4
#suk222, tz638
#Shehroze Umer Khan & Tarik Zulfikarpasic

import time
import random

class Board():
    #Initialising the board; it is going to be used only once
    def __init__(self):                                                              
        self.coinlist=[]
        self.lista=[]
        for i in range(6):
            a = []
            for j in range(7):
                a.append(' ')
            self.lista.append(a)
            
    #To update the board after every move. This returns the whole board, which is going to be used for every turn
    def update_board(self, coin, y, x):                                              
        self.lista[y][x - 1] = coin    
        return self.lista                                                            
    
    #Coins are added to the list called coinlist and are later displayed in self.display()
    def add_to_the_list(self,coin):                                                  
        self.coinlist.append(coin)
        return self.coinlist
    
    #This checks which row is free to occupy
    def check_board(self,x):                                                         
        for i in range(6):
            if self.lista[i][x-1] !=' ':
                #If the loop comes across the occupied space, it returns the number of row before it                                             
                return i-1
        else:
            #Otherwise, if there are no occupied cells in the column, it returns the bottom
            return i                                                                
    
    #This method takes the result of check_board() and returns the respective y-coordinate in Processing
    def dt_pos(self,i):                                                              
        if i == 0:
            return 35
        elif i == 1:
            return 105
        elif i == 2:
            return 175
        elif i == 3:
            return 245
        elif i == 4:
            return 315
        elif i == 5:
            return 385
        
    #This iterates through the list of coins and displays them in draw
    def display(self):                                                               
        for i in self.coinlist:
            i.display()
            i.move()

#This class is essential in determining the winner            
class Winner():                                                                      
    def __init__(self, board,player):
        self.board=board
        self.player=player
        self.counter=0
        
    """This method takes row as an argument and checks by slicing if there are 4 consecutive same coins anywhere in the row
    it will essentially take diagonals and columns as argument and check for matches 
    7,6,5 and 4 are the only possible row lengths that produce the winner"""
    def check_row(self, row, player):                                                
                                                                                     
        if len(row) == 7:                                                            
            self.counter=0
            for j in range(4):
                for i in row[j:(j+4)]:
                    if i==' ' or i.colour != colours(self.player):
                        self.counter+=1
                        break
            #The idea here is that, for 4 slices, we expect self.counter to be 4 if there is no winner
            if self.counter==4:                                                      
               #If it is different than 4, then there is a winner                                                             
                return False                                                         
            else:
                return True
                #This holds for all if-statements in the method, but expected self.counter is equal to the number of the slices
                
        elif len(row) == 6:
            self.counter=0
            for j in range(3):
                for i in row[j:j+4]:
                    if i==' ' or i.colour != colours(self.player):
                        self.counter+=1
                        break
            if self.counter==3:
                return False
            else:
                return True
            
        elif len(row) == 5:
            self.counter=0
            for j in range(2):
                for i in row[j:j+4]:
                    if i==' ' or i.colour != colours(self.player):
                        self.counter+=1
                        break
            if self.counter==2:          
                return False
            else:
                return True
            
        elif len(row) == 4:
            self.counter=0
            for i in row:
                if i==' ' or i.colour != colours(self.player):
                    return False
            return True
    
    #This method in most of the cases transforms columns and diagonals in rows and later passes them as arguments to check_row
    def winner(self, board):
    
        #For row
        for row in board:
            if self.check_row(row, self.player):
                return True
    
        c = len(self.board)
        
        #For column
        for i in range(c+1):
            col = []
            for j in range(c):
                col.append(board[j][i])
            if self.check_row(col, self.player):
                return True
        
        #For all diagonals
        left = []
        right = []

        l = []
        r = []
        l1 = []
        r1 = []
        l2 = []
        r2 = []
        l3 = []
        r3 = []
        l4 = []
        r4 = []
        l5 = []
        r5 = []
        
        for i in range(c):
            l.append(board[i][i])
            r.append(board[i][-i-1])
            l3.append(board[i][i+1])
            r3.append(board[i][-i-2])
    
        for i in range(c-1):
            l1.append(board[i+1][i])
            r1.append(board[i+1][-i-1])
            l4.append(board[i][i+2])
            r4.append(board[i][-i-3])
    
    
        for i in range(c-2):
            l2.append(board[i+2][i])
            r2.append(board[i+2][-i-1])
            l5.append(board[i][i+2])
            r5.append(board[i][-i-4])
    
        left.append(l)
        left.append(l1)
        left.append(l2)
        left.append(l3)
        left.append(l4)
        left.append(l5)
    
        right.append(r)
        right.append(r1)
        right.append(r2)
        right.append(r3)
        right.append(r4)
        right.append(r5)
    
        for diagonal in right:
            if self.check_row(diagonal, self.player):
                return True
        for diagonal in left:
            if self.check_row(diagonal, self.player):
                return True
    
        return False
    
    #This sets flag variable to 0 if there is a winner
    def displaywinner(self):                                         
        if self.winner(self.board):                                  
            flag=0
        return flag
        #The variable is used for reference in the gameplay to display the graphics for a winner    
            
class Coin:
    def __init__(self, xp, finalyp, colour):
        #xp will be determined dynamically, by keypressed function                              
        self.xp = xp 
        #yp is always 0                                                
        self.yp = 0 
        #Velocity is 35 because Processing y-coordinates are multiples of 35 and also because we want to center tokens on the grid each time.                                                 
        self.v = 35
        self.colour = colour
        #finalyp will be the next available spot in the list of lists (when converted into processing coordinate in the dt_pos method in Board class)
        self.final = finalyp
    
    #Moving is pretty straightforward, y-coordinate is increased by velocity until the final, desired coordinate is reached, then velocity becomes 0.        
    def move(self):                                           
        self.yp += self.v
        if self.yp == self.final:
            self.v = 0
            
    def display(self):                                               
        #Creating coins depending on the colour
        if self.colour == "red":
            fill(255,0,0)
        elif self.colour== "yellow":
            fill(255,255,0)        
        ellipse(self.xp, self.yp, 50,50)
        
class Turn:
    def __init__(self):
        self.key_typed = 0
        self.coord = 0
        self.helper=0
        #Measuring the time since the beginning of the game because timer needs to be defined in every moment
        #The main reference timer will be in keyPressed function and is delivered when ENTER is pressed
        self.timer=time.clock()
        #To arbitrarily chose who plays first
        self.turn = 1
        #This list is used to display the timer during the game. It calculates the difference between the current time at every draw() refresh and the beginning of the turn (see keyPressed)
        self.timelist=[0] 
        
class Counter:
    def __init__(self):
        self.value=1


#This function determines the player given the turn
def who_plays(turn):                                                 
    player=1-turn%2
    return players[player]

#This function returns the colour of the player obtained by who_plays function. The result is crucial in instantiating coins
def colours(player):                                                 
    colour1=player["colour"]                                         
    return colour1

#This function instantiates the coin given the x-coordinate, y-coordinate and color
def coins(x, y, colour):                                             
    a = Coin(x, y, colour)
    return a
def gameplay(b,turn,coord):
    
    #This calculates which row in the given column is free to occupy
    y = int(b.check_board(int(current_turn.key_typed)))
    
    #This is the value of y-coordinate Processing understands given the index in the list              
    finaly = b.dt_pos(y)
    
    #Gives the name of the player        
    player = who_plays(current_turn.turn)
    
    #Gives the colour of the desired coin given the player and the result is passed to the function creating the coins.                                            
    colour1=colours(player)
                                        
    coin = coins(current_turn.coord,finaly,colour1)
    
    #adds the coin to the list so that it can be displayed later in b.display()
    b.add_to_the_list(coin)                                          
    
    #Updating the board everytime and using the updated version in the same function, recursively    
    b = b.update_board(coin, y, int(current_turn.key_typed))
    
    #instantiating the Winner object
    winner2 = Winner(b, player)
    #winner3 is a boolean which shows if there is a winner or not                                      
    winner3 = winner2.winner(b)                                      
    if winner3:
        #if there is a winner, flag variable is returned and is used later in the draw function
        a= winner2.displaywinner()
        return a                           
    #otherwise, the game continues on the updated board    
    return b                                                         

#Defining keypressed and turning keys into meaningful x-coordinates
def keyPressed():                                                    
    coord = 0
    lis = ['1', '2', '3', '4', '5', '6', '7']
    
    #The following lines of code stop the first display message of introduction
    if key==ENTER:
        #Helper variable helps to control the gameplay - display of help message and the game itself
        current_turn.helper+=1 
        #This is done in order to have the actual game started at the moment ENTER is pressed to cancel the help message
        #IF condition is here in order to prevent multiple pressing of ENTER influencing the timer
        if current_turn.helper==1:
            current_turn.timer=time.clock()
    
    #Current_turn.helper condition is added in order to prevent start of the game before display message is canceled    
    if key in lis and current_turn.helper>=1:
        if (key == '1'):
            coord=40
        elif (key == '2'):
            coord= 120
        elif (key == '3'):
            coord= 200
        elif (key == '4'):
            coord= 280
        elif (key == '5'):
            coord= 360
        elif (key == '6'):
            coord= 440
        elif (key == '7'):
            coord= 520
        
        
        #The variable current_turn.key_typed represents the value of key pressed, it was previously set to 0 to avoid Errors    
        current_turn.key_typed = key 
    
    if current_turn.key_typed in count:
        count[current_turn.key_typed] += 1
    else:
        count[current_turn.key_typed] = 1 
    
    #This IF condition ensures that trying to populate the full column doesn't stop timer
    if count[current_turn.key_typed]<8:
        current_turn.timer=time.clock()
        #Reseting timelist to 0 when new player gets the turn
        current_turn.timelist=[0] 
        
    #The variable current_turn.coord represents the value of coord, it was previously set to 0 to avoid Errors
    current_turn.coord = coord         
    
b = Board()
def setup():
    #A lot of variables are defined here globally because the python module isn't developed enough
    #Therefore, we need to use them in the global scope
    size(560,480)
    frameRate(20)
    global current_turn
    current_turn = Turn()
    global turn
    global counter
    counter=Counter()
    global count
    count = {}

    
def draw():
    global coin
    global counter
    global g
    global bg
    global player
    global timeit   
    
    #These lines of code are constantly executed in draw() until ENTER is pressed        
    if current_turn.helper==0:
        bg=loadImage("bg3.jpg")
        image(bg,0,0,560,480)
        textSize(14)
        text("Welcome to Connect 4. This is a two-player game played on 7x6 grid.", 10,30)
        text("Players take alternating turns in placing colored tokens on the grid.", 10, 60)
        text("The goal of the game is to place four tokens of the same color either ", 10,90)
        text("vertically, horizontally, or diagonally.", 10, 120)
        text("To place a token in the desired column, press a number from 1 to 7." ,10,150)
        text("Then, it will be placed automatically in an available spot in the chosen column.", 10,180)
        text("If you finished reading this message and want to proceed, press ENTER.", 10,210)
        ss1=loadImage("ss1.png")
        ss2=loadImage("ss2.png")
        ss3=loadImage("ss3.png")
        image(ss1,5,245,180,200)
        image(ss2,190,245,180,200)
        image(ss3,375,245,180,200)
    
    #These lines start being executed since the first ENTER press
    if current_turn.helper>=1:
        bg=loadImage("bg3.jpg")
        image(bg,0,0,560,480)
        stroke(255)
        strokeWeight(1.5)
        #Vertical Lines
        line(80,0,80,420)
        line(160,0,160,420)
        line(240,0,240,420)
        line(320,0,320,420)
        line(400,0,400,420)
        line(480,0, 480, 420)
        #Horizontal Lines
        line(0,70, 560, 70)
        line(0,140, 560, 140)
        line(0,210, 560, 210)
        line(0,280, 560, 280)
        line(0,350, 560, 350)
        line(0, 420, 560, 420)
        
        #The game is played only if a key is pressed, a turn is between 0 and 43, and the column is not full
        if current_turn.key_typed > 0 and 0 < current_turn.turn <= 43 and count[current_turn.key_typed] < 7:
            #Calling gameplay function
            g=gameplay(b,current_turn.turn,current_turn.coord)
            #Calling the function to measure the time taken for the move
            #Assigning the player who plays to the variable
            player=who_plays(current_turn.turn)
            #Subtracting the time taken from the player's total time
            #Turn is incremented by 1                   
            current_turn.turn+=1
            #The value of key is set to 0 so that coins don't move around the board because draw() is continuous                                  
            current_turn.key_typed=0
            
        #This displays all the coins in the coinlist                                  
        b.display()
        #s is the time difference between the moment of the draw() refresh and the beginning of the turn
        s=time.clock()-current_turn.timer 
        #That value is appended to our timelist   
        current_turn.timelist.append(s)
        #Time_elapsed is the difference between the two last (integer) members in the timelist, it is either 1 0r 0.
        #That value is always subtracted from the player's remaining time in the dictionary
        time_elapsed=int(current_turn.timelist[-1])-int(current_turn.timelist[-2])
        
        #This part of graphics warns the users who is playing next and what is their remaining time                                                                                       
        if who_plays(current_turn.turn) == p1:
            p1["time"]=p1["time"]-int(time_elapsed)
            textSize(24)                                          
            fill(255,255,0)
            text('Yellow\'s turn! You have '+str((p1["time"])/60)+'min '+str((p1["time"])%60)+' sec remaining.', 5, 460)
            
        elif who_plays(current_turn.turn)  == p2:
            p2["time"]=p2["time"]-int(time_elapsed)
            textSize(24)
            fill(255,0,0)
            text('Red\'s turn! You have '+str((p2["time"])/60)+'min '+str((p2["time"])%60)+' sec remaining.', 20, 460)
            
        if p1["time"]<=0:
            g=0
            player=p2
            
        elif p2["time"]<=0:
            g=0
            player=p1
        
        #If there is a winner, g=flag variable=0, here we check if that is the case
        if g==0:                                                  
            current_turn.turn=0
            #If it is, set turn to 0 and stop the gameplay                                   
        
        if current_turn.turn==0:                                  
            #If the gameplay is stopped, there must be a winner, this part uses variable player to print appropriate message
            if player==p1:
                img=loadImage('winner.jpg')
                image(img, 0,0,560,420)
                image(bg,0,420,560,480)
                textSize(24)
                fill(255,255,0)
                text("Congratulations, Yellow wins!",100,460)
            elif player==p2:
                img=loadImage('winnerred.jpg')
                image(img, 0,0,560,420)
                image(bg,0,420,560,480)
                textSize(24)
                fill(255,0,0)
                text("Congratulations, Red wins!",100,460)
        
        #When turn reaches 43 (the maximum number of turns is 42), and there is no winner, the game is tied and an appropriate message with picture is displayed
        if current_turn.turn>=43 and g != 0:                                
            tie=loadImage("gameover.png")
            image(tie, 0,0,560,480)
            textSize(24)
            fill(255,255,255)
            text("Sorry, it's a draw.",180,460)
        
#The players who will play:
p1={"time": 180, "colour": 'yellow'}
p2={"time": 180, "colour": 'red'}
players = [p1, p2]
