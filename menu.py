import auxiliarFunctions as aux
import snakeRecord as sr
import gameLoop as gl
import msvcrt as keys
import time
import copy
import os


class title:
    def __init__(self, aString, height = 0, center = True):
        self.baseTitle = aString
        self.title = aString
        self.selected = False
        self.height = height
        self.center = center
    
    
    def select(self):
        # Adds the lines '- titleHere -' to the string representing title.
        self.selected = True
        self.title =  str("- " + self.baseTitle + " -")
        

    def unselect(self):
        # Takes lines '- titleHere -' out from the string representing title.
        self.title =  str(self.baseTitle)
        self.selected = False


class menu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = aux.drawBorders(aux.createScreen(self.width, self.height))
        self.titles = []
    

    def clearGrid(self):
        # Sets self.grid to an empty grid I(with border).
        self.grid = aux.drawBorders(aux.createScreen(self.width, self.height))


    def drawTitle(self, title):
        # Draw a title (object) on self.grid.
        height = title.height + 1 # Index correction for grid borders.

        if title.center: # If the title is to be centered
            start = int((self.width/2) - (len(title.title)/2))
            for i in range(len(title.title)):
                self.grid[height][i+start] = title.title[i]

        else: # If not to be centered.
            for i in range(len(title.title)):
                self.grid[height][i+1] = title.title[i]


    def printGrid(self):
        # Clears, draws titles on and prints grid.
        self.clearGrid()
        self.drawTitles()
        print(("".join("".join(e for e in row)+"\n" for row in self.grid)))


    def drawTitles(self):
        # Draws titles on grid.
        for title in self.titles:
            self.drawTitle(title)


    def addTitle(self, title):
        # Adds title instance to titles list.
        self.titles.append(title)


    def switch(self, key):
        # Simulates the selection of titles on menu.
        # Takes int representing key as an argument.
        ind = 0

        for title in self.titles:
            if title.selected: # To find current selected title.
                if key == 13: # If enter has been pressed.
                    self.pressedEnter(title)
                title.unselect()# Removes selection of title.
                ind = self.titles.index(title) # Registers index of selected title.
        try:
            if key == 72: # up key
                self.titles[ind - 1].select()
            elif key == 80:# down key
                self.titles[ind + 1].select()
        except:
            pass


    def pressedEnter(self, title):
        # User pressed enter on menu. Called from self.switch.
        # Takes title.
        if "PLAY" in title.title:
            os.system("cls")
            gl.gameLoop()

        elif "HIGHEST SCORES" in title.title:
            highestScores()

        elif "QUIT" in title.title:
            quit()
        
        elif "BACK" in title.title:
            mainMenu()




def highestScores():
    # Highest scores menu.
    scoresScreen = menu(20, 20)
    scores = sr.getScores()
    scores.sort(key = aux.third, reverse = True)

    scoresScreen.addTitle(title("DATE/NAME/SCORE", height = 1))


    for i in range(len(scores)):
        if i > 10:
            break
        scoresScreen.addTitle(title(scores[i][1] + " " + scores[i][3] + " " + str(scores[i][2]), height = i+4))

    scoresScreen.addTitle(title("BACK TO MENU", height = scoresScreen.height - 4))
    scoresScreen.titles[-1].select()

    while 1:

        if keys.kbhit():
            dir = keys.getch()
            while keys.kbhit():
                dir = keys.getch()
            scoresScreen.switch(ord(dir))

        time.sleep(0.08)
        aux.move_cursor()
        scoresScreen.printGrid()
    


def mainMenu():
    # Create instance of menu class.
    mainM = menu(20,20)

    # Create instances of title class.
    titles = [("MAIN MENU",1),
    ("PLAY", 3),
    ("HIGHEST SCORES",4),
    ("OPTIONS",5),
    ("QUIT",6)]

    # Adding title objects to menu.
    for element in titles: 
        mainM.addTitle(title(element[0], height = element[1]))

    mainM.titles[1].select()

    # Mainloop.
    while 1:
        time.sleep(0.08)
        if keys.kbhit():
            dir = keys.getch()
            while keys.kbhit():
                dir = keys.getch()
            mainM.switch(ord(dir))

        aux.move_cursor()
        mainM.printGrid()


if __name__=="__main__":
    mainMenu()