import ctypes
from ctypes import wintypes

WIN32  = ctypes.WinDLL("kernel32")
stdout = WIN32.GetStdHandle(-11)
COORD = wintypes._COORD

def move_cursor(pos=(0,0)):
    WIN32.SetConsoleCursorPosition(stdout, COORD(*pos))

def drawBorders(grid):
    """Draws limits of map."""
    char = "#"
    grid[0] = [char for i in grid[0]]
    grid[-1] = [char for i in grid[0]]

    for i in grid:
        i[0] = char
        i[-1] = char

    return grid

def createScreen(x,y, base = " "):
    return [[base for e in range(x)] for i in range(y)]

def third(x):
    return x[2]



