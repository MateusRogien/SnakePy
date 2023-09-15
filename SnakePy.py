import time
import random

class Snake:
    def __init__(self, size, speed, boardWidth, boardHight):
        self.size = size
        self.speed = speed
        self.boardHight = boardHight
        self.boardWidth = boardWidth
        self.snakeArray = [[18, 3], [19, 3], [20, 3], [21, 3], [22, 3], [23, 3]]
        # self.snakeArray = [[2,3],[3,3],[4,3],[5,3],[6,3]]
        self.direction = "front"
        self.directionBuffer = ""
        self.target = [8, 3]
        self.score = 0
        self.grow = False


    def __del__(self):
        print ('\nHope you enjoyed playing!') 

    def checkIfCrached():
        pass
    
    def checkIfEat():
        pass
    
    
    #Check a buffer variable, if empty moves the snake in the direction of the previous move variable,if not empty it will move the snake to the direction, empty the buffer and copy the move to previous move buffer.            
    def moveSnake(self,direction): 
            if direction == "right":
                x = (self.snakeArray[-1][0]) + 1
                y = self.snakeArray[-1][1]
            elif direction == "left":
                x = (self.snakeArray[-1][0]) - 1
                y = self.snakeArray[-1][1]
            elif direction == "up":
                x = (self.snakeArray[-1][0])
                y = self.snakeArray[-1][1] - 1     
            elif direction == "down":
                x = (self.snakeArray[-1][0])
                y = self.snakeArray[-1][1] + 1
            else:
                print ("Fatal Error!") 
                exit()
            if self.snakeArray[-2] != [x, y]:
                self.VerifyCapture()
                if self.grow == True:                   
                    self.grow = False 
                else:
                    self.snakeArray.pop(0)   
                self.snakeArray.append([x,y])
                self.direction = direction
                if self.detectDealth() == True:
                    print ("Game Over!")
                    exit()
            return                         


    #Prints the board
    def printBoard(self):
        print ("Score =" + str(self.score) )
        for y in range(self.boardHight):
          print ("")
          for x in range(self.boardWidth):
                #Print Walls
                if y == 0 or y == self.boardHight -1 :
                    print ('⎯', end="")
                elif x == 0 or x == self.boardWidth -1:
                    print ('|', end="")
                else:
                    isSnake = False
                    for i in self.snakeArray:
                        if i == [x,y]:
                            isSnake = True
                    if isSnake == True:
                        print ("*",end="")
                    elif [x , y] == self.target:
                        print ("@", end="")                   
                    else:
                        print (" ",end="")
        print (self.snakeArray)         

    #Generates a random number, verifies it is not coliding with the snakearray.        
    def generateTarget(self):
        while True:
            x = random.randrange(1,self.boardWidth,1)
            y = random.randrange(1, self.boardHight,1)
            if self.snakeArray.count([x,y]) == 0:
                self.target = [x, y]
                break
        

    def VerifyCapture(self):
        if self.target == self.snakeArray[-1]:
            self.score += 1
            self.grow = True
            self.generateTarget()
    
    def detectDealth(self):
        if self.snakeArray.count(self.snakeArray[-1]) == 2:
            return True
        elif self.snakeArray[-1][0] == 0 or self.snakeArray[-1][0] == self.boardWidth:
            return True
        elif self.snakeArray[-1][1] == 0 or self.snakeArray[-1][1] == self.boardHight - 1 :
            return True
        else:
            return False
    


snake = Snake (4, 5, 30, 15)

while(1):
    snake.printBoard()
    direction = input ("")
    snake.moveSnake(direction)



