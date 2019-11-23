import screenClass as sc
import classSnake as cs
import msvcrt as keys
import snakeRecord
import time
import menu
import os


def getUserName():
    # Asks the user to input their user name if score was good enough.
    name = input("Enter your name:\n> ")
    while len(name) > 5:
        name = input("Enter your name:\n> ")
    
    return name


def gameLoop():
    screen = sc.screen()
    snake = screen.snake

    while True:
        time.sleep(screen.speed)

        if keys.kbhit() and snake.canTurn:
            snake.canTurn = False
            dir = keys.getch()
            while keys.kbhit():
                dir = keys.getch()
            snake.changeDirection(ord(dir))
            snake.canTurn = True

        if screen.losed:
            time.sleep(1)
            if len(screen.bestScores) <= 1:
                snakeRecord.recordScore(screen.score, getUserName())
            elif screen.score > screen.bestScores[-1][2]:
                snakeRecord.recordScore(screen.score, getUserName())
            os.system("cls")
            menu.mainMenu()
        else:
            snake.move(grow=screen.gotFood())
            if snake.outOfMap(screen) or snake.ateSelf():
                screen.losed = True
                continue
            
            screen.printScreen()


if __name__=="__main__":
    gameLoop()