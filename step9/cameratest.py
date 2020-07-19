# Some simple tests for the camera class
# adapt and change as you like
# Discount Mars Rover Project , 2019

from camera import Camera

c = Camera(1800,1024, 1)
c.setResolution(800,600)

img = c.getImage()

c.getAndStoreImage()

c.setResolution(1800,1000)
c.getAndStoreImage()

