from snakeRecord import highestScores
import auxiliarFunctions as aux
import classSnake as cs
from os import system
import random
import copy

class screen:
    def __init__(self):
        self.snake = cs.snake()
        self.speed = 0.1
        self.width = 20
        self.height = 20
        self.blank_grid = aux.drawBorders([[" " for x in range(self.width)] for y in range(self.height)])
        self.score = 0
        self.food = (random.randint(1, self.height-2), random.randint(1, self.width-2))
        self.losed = False
        self.bestScores = highestScores()
        self.highest = self.bestScores[0]


    def getFoodCoordinates(self):
        # Generates new food coordinates. Makes sure they are not over the snake's body.
        while self.food in self.snake.body:
            self.food = (random.randint(1, self.height-2), random.randint(1, self.width-2))
        return self.food


    def gotFood(self):
        # Checks if snake got food.
        if self.snake.body[0] == self.food:
            self.score += 1
            self.food = self.getFoodCoordinates()
            return True
        else:
            return False


    def printScreen(self):
        # Prints screen, takes snake object.
        aux.move_cursor()
        grid = copy.deepcopy(self.blank_grid)

        for part in self.snake.body:# Drawing snake.
            grid[part[0]][part[1]] = "#"
            grid[self.food[0]][self.food[1]] = "Q" # Drawing food.

        screen_string = ("".join("".join(e for e in row)+"\n" for row in grid))
        try:
            print("SCORE: ", self.score, "HIGHEST: ", self.highest[2])
        except:
            print("SCORE: ", self.score)
        print(screen_string)

