class Snake:
    def __init__(self, size, speed, boardWidth, boardHight):
        self.size = size
        self.speed = speed
        self.boardHight = boardHight
        self.boardWidth = boardWidth
        self.snakeArray = [[2,3],[3,3],[4,3]]
        self.direction = "front"
        self.directionBuffer = ""
    
    def __del__(self):
        print ('\nHope you enjoyed playing!') 

    def checkIfCrached():
        pass
    
    def checkIfEat():
        pass


    def moveSnake(self,Direction): #Check a buffer variable, if empty moves the snake in the direction of the previous move variable,if not empty it will move the snake to the direction, empty the buffer and copy the move to previous move buffer. 
            if Direction == "front":
                self.snakeArray.pop(0)
                x = (self.snakeArray[-1][0]) + 1
                y = self.snakeArray[-1][1]
                self.snakeArray.append([x,y])
            elif Direction == "left":
                self.snakeArray.pop(0)
                x = (self.snakeArray[-1][0]) - 1
                y = self.snakeArray[-1][1]
                self.snakeArray.append([x,y])
            elif Direction == "up":
                self.snakeArray.pop(0)
                x = (self.snakeArray[-1][0])
                y = self.snakeArray[-1][1] - 1
                self.snakeArray.append([x,y])     
            elif Direction == "down":
                self.snakeArray.pop(0)
                x = (self.snakeArray[-1][0])
                y = self.snakeArray[-1][1] + 1
                self.snakeArray.append([x,y])                           


    #Prints the board
    def printBoard(self):
        for y in range(self.boardHight):
          print ("")
          for x in range(self.boardWidth):
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
                    else:
                        print (" ",end="")          
        


snake = Snake (4, 5, 30, 15)

snake.printBoard()
snake.moveSnake("down")
snake.printBoard()
print (list(snake.snakeArray))