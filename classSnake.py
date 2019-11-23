
class snake:

    def __init__(self, body = [(1,4),(1,3),(1,2)]):
        self.body = [(1,4),(1,3),(1,2)]
        self.direction = "right"
        self.canTurn = True


    def outOfMap(self, screen):
        # Checks if snake is out of the map.
        yh = self.body[0][0]
        xh = self.body[0][1]

        return (1 > yh) or (yh > screen.height - 2) or (1 > xh) or (xh > screen.width - 2)


    def move(self, grow=False):
        # Motion, creates copy of head but changes it according to
        # direction. Then deletes tail. Modifies snake variable (list).
        y, x = self.body[0]

        if not grow:
            self.body.pop()
        
        d = {"right":(y,x+1), "left":(y,x-1),
            "down":(y+1,x), "up":(y-1,x)}
        
        self.body = [d[self.direction]] + self.body


    def ateSelf(self):
        # Checks if snake ate itself.
        return self.body[0] in self.body[1:]
    

    def changeDirection(self, key):
        # Changes direction variable.
        
        directions = dict({72: "up", 80: "down",
                    75: "left", 77: "right"})

        oposites = dict({"up":"down","left":"right","right":"left","down":"up"})    

        if key in directions:
            if oposites[directions[key]] != self.direction:
                self.direction = directions[key]
