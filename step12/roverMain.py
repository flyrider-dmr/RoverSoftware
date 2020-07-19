import paho.mqtt.client as mqtt
from rover import Rover
import time
from map import Map

rover = Rover(0,0)
map = Map()
map.dummyData() 

def messageReceived(client, userdata, message):
    datas = message.payload.decode("utf-8")
    # get first number for command
    text = datas.split(':')
    commands = text[0]
    command = int(commands)
    print("Command received :" , str(datas))
    if command == 1:
        # request for rover status information
        message = rover.statusInfo()
        client.publish("marsrover/statusinfo", message) 

    if command == 2:
        # request for image
        message = rover.camera.getImage()
        client.publish("marsrover/image", message) 

    if command == 3:
        # request for map information
        message = map.toString()
        client.publish("marsrover/map", message) 

    if command == 4:
        # set drive mode to autonomous
        rover.stop()
        rover.setAutonomousDrive()
        
    if command == 5:
        # new waypoint sent - store waypoint
        # split in lines
        text = datas.split(':')
        x = text[1]
        y = text[2]
        name = text[3]
        map.storeWayPoint(x,y,name)

    if command == 6:
        rover.stop()
        rover.resetAutonomousDrive()
    
    # camera commands
    
    if command == 7:
        text = datas.split(':')
        angle = text[1]
        rover.camera.turnRight(angle)

    if command == 8:
        text = datas.split(':')
        angle = text[1]
        rover.camera.turnLeft(angle)

    if command == 9:
        text = datas.split(':')
        angle = text[1]
        rover.camera.turnUp(angle)

    if command == 10:
        text = datas.split(':')
        angle = text[1]
        rover.camera.turnDown(angle)

    if command == 12:
        # command to lower down the drill to a position with offset to X , Y
        # compared to standard 0,0 position
        text = datas.split(':')
        x = text[1]
        y = text[2]
        rover.lowerDrill(x,y)
        #print("lower drill to " + str(x) + " , " + str(y))
        
    if command == 13:
        # command to raise up the humidity sensor
        rover.raiseDrill()
        
    if command == 14:
        # drive forward
        rover.forwardDrive()
    
    if command == 15:
        # drive backward
        rover.backwardDrive()
        
    if command == 16:
        # left turn
        rover.turnLeft()
        
    if command == 17:
        # right turn
        rover.turnRight()             
        
    if command == 18:
        # EMERGENCY ONLY : rover has to stop
        rover.stop()

# MTTQ broker setup
broker_address="localhost"

client = mqtt.Client("Rover") #create new instance
client.on_message=messageReceived #attach function to callback
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop

client.subscribe("marsrover/command")

while True:
    time.sleep(1) # wait
#client.loop_stop() #stop the loop


  