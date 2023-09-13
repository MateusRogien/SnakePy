class Snake:
    def __init__(self, size, speed, boardWidth, boardHight):
        self.size = size
        self.speed = speed
        self.boardHight = boardHight
        self.boardWidth = boardWidth
        self.snakeArray = [[2,boardHight-2],[3,boardHight-2]]
    
    def __del__(self):
        print ('\nHope you enjoyed playing!') 

    def checkIfCrached():
        pass
    
    def checkIfEat():
        pass

    def moveSnake(): #Check a buffer variable, if empty moves the snake in the direction of the previous move variable,if not empty it will move the snake to the direction, empty the buffer and copy the move to previous move buffer. 
        pass 
    
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
                    print (' ', end="")
            
        


snake = Snake (4, 5, 30, 15)
print (snake.size)

snake.printBoard()