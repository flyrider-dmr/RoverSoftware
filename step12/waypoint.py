# WayPoint
# Respresents one waypoint. Waypoints get received from the control center
# Each waypoint has coordinates and a name for better orientation

class WayPoint:
    
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        
    def toString(self):
        ret = "W:" + str(self.x) + ":" +  str(self.y)  + ":" +  str(self.name) + ";"
        #retbs = ret.encode("UTF-8")
        return ret
