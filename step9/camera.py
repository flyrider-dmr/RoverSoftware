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
        self.resY = resX
        self.timeout = timeout

    def getAndStoreImage(self):
        #filename with daten and time
        x = datetime.datetime.now()
        datenandtime = x.strftime("%c")
        filename = "/home/pi/Desktop/ {} .jpg"
        filename = filename.format(datenandtime).strip().replace(" ","")
        self.camera.resolution = (self.resX, self.resY)
        self.camera.framerate = 15
        sleep(self.timeout)
        self.camera.capture(filename)
        
    def getImage(self):
        self.camera.resolution = (self.resX, self.resY)
        self.camera.framerate = 15
        stream = BytesIO()
        img = self.camera.capture(stream, 'jpeg')
        byteS = stream.read()
        return byteS
        
        
    def setResolution(self, resX, resY):
        self.camera.resolution = (self.resX, self.resY)
    
    def setMode(self, mode):
        if mode == 1:
            self.camera.image_effect = 'sketch'
