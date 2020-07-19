# the rover itself
# estX : estimated X coordinate (in cm from starting point 0,0)
# estY : estimated Y coordinate

import threading, time, math
from camera import Camera

class Rover:
       
    def __init__(self, estX, estY):
        self.estX = 0
        self.estY = 0
        self.speed = 0
        self.rotX = 0
        self.drillUp = 1 # drill is up (1) or down (0)
        self.drillX = 0  # drill offset to X coordinates (forward direction)
        self.drillY = 0  # drill offset to Y coordinates (side direction)
        self.autonomous = 0
        self.TIMERSECONDS = 2
        self.updateRoverStatus()
        self.camera = Camera(1000,600, 3) # resolution on the client side expected as 1000 x 600

    def updateRoverStatus(self):
        # update position and estimated direction according to current drive status
        # at full speed the rover runs 10cm per second
        distanceSinceLast =  int(self.speed * 3 / 100)
        rotationABS = math.fabs(self.rotX)
        distX = distanceSinceLast * math.cos(math.radians(rotationABS))
        distY = distanceSinceLast * math.sin(math.radians(rotationABS))
        self.estX = int(self.estX + distX)
        if self.rotX >= 0:
            self.estY = int(self.estY - distY)
        else:
            self.estY = int(self.estY + distY)
        print(self.estX , self.estY)
        threading.Timer(self.TIMERSECONDS , self.updateRoverStatus).start()         
        

    def statusInfo(self):
        #ret = str(self.estX) + ":" +  str(self.estY)
        ret = str(self.estX) + ":" +  str(self.estY)  + ":" +  str(self.speed) + ":"
        ret = ret + str(self.rotX)+ ":" + str(self.drillUp) + ":" + str(self.autonomous)
        ret = ret + ":" + self.camera.info()
        return ret
    
    def setAutonomousDrive(self):
        self.stop()
        self.autonomous = 1
    
    def resetAutonomousDrive(self):
        self.stop()
        self.autonomous = 0
    
    def forwardDrive(self):
        self.speed = 100
       
    def backwardDrive(self):
        self.speed = -50
        
    def turnLeft(self):
        self.rotX = self.rotX - 45
        
    def turnRight(self): 
        self.rotX = self.rotX + 45    
    
    def stop(self):
        self.speed = 0
    
    def lowerDrill(self, x, y):
        self.drillUp = 0
        self.drillX = x
        self.drillY = y
        # TO DO Command needs to be issued to Arduino
        
    def raiseDrill(self):
        self.drillUp = 1