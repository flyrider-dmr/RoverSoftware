# Class representing the raspberry pi camera 
# Discount Mars Rover Project , 2019

from picamera import PiCamera
from time import sleep
import datetime
from io import BytesIO

class Camera:  
    def __init__(self, resX, resY, timeout):
        self.camera = PiCamera()
        self.resX = resX
        self.resY = resY
        self.timeout = timeout
        self.pitchAngle = 0
        self.turnAngle = 0

    def getAndStoreImage(self):
        #filename with daten and time
        x = datetime.datetime.now()
        datenandtime = x.strftime("%c")
        filename = "/home/pi/Desktop/ {} .jpg"
        filename = filename.format(datenandtime).strip().replace(" ","")
        sleep(self.timeout)
        self.camera.capture(filename)
        
    def getImage(self):
        filename = "/home/pi/Desktop/current.jpg" 
        self.camera.capture(filename)
        f=open(filename, "rb") 
        fileContent = f.read()
        message = bytearray(fileContent)
        return message
        
        
    def setResolution(self, resX, resY):
        self.camera.resolution = (resX, resY)
    
    def setMode(self, mode):
        if mode == 1:
            self.camera.image_effect = 'sketch'

    def turnRight(self, angle):
        self.turnAngle =  angle
        print("Camra turn right: " + str(turnAngle))

    def turnLeft(self, angle):
        self.turnAngle = -angle

    def turnUp(self, angle):
        self.pitchAngle =  angle

    def turnDown(self, angle):
        self.pitchAngle =  -angle

    def info(self):
        ret = str(self.turnAngle) + ":" +  str(self.pitchAngle)  
        return ret