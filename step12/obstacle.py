class Obstacle:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def toString(self):
        ret = "O:" + str(self.x) + ":" +  str(self.y) + ";"
        #retbs = ret.encode("UTF-8")
        return ret