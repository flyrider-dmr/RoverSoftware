# The map for the rover navigation
# contains waypoints sent from the control center and
# obstacles detected by the rover

from waypoint import WayPoint
from obstacle import Obstacle 

class Map:
    
    def __init__(self):
        self.waypoints = []
        self.obstacles = []
        self.waypoints.append(WayPoint(0,0,"START"))
        
    def storeWayPoint(self, x, y, text):
        point = WayPoint(x,y,text)
        self.waypoints.append(point)
        
    def storeObstacle(self, x, y):
        point = Obstacle(x,y)
        self.obstacles.append(point)
        
    def toString(self):
        text = ""
        for point in self.waypoints:
            text = text + point.toString()
        for point in self.obstacles:
            text = text + point.toString()
        return text

    def dummyData(self):
        self.waypoints.append(WayPoint(100,23, "Rim"))
        self.waypoints.append(WayPoint(150,-23, "Crater"))
        self.waypoints.append(WayPoint(250,2, "Target"))
        self.obstacles.append(Obstacle(230,122))
        self.obstacles.append(Obstacle(280,243))
        self.obstacles.append(Obstacle(350,23))
            