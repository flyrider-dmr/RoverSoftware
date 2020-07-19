

#include "DriveControl.h"

DriveControl dc;
int readValue = 0;

void setup() {
  // put your setup code here, to run once:
    Serial.begin(9600);
    Serial.println("Discount Rover drive test is ready..." );
    Serial.println("Go forward    : 1" );
    Serial.println("Go backward   : 2" );
    Serial.println("Turn right    : 3" ); 
    Serial.println("Turn left     : 4" );  
    Serial.println("Curve right   : 5" );  
    Serial.println("Curve left    : 6" );    
    Serial.println("Stop          : 8" );   
}

void serialEvent()
{
      readValue   = Serial.parseInt();
   
      if(readValue == 8)
      {
        Serial.println("Stop" ); 
        dc.stop();
      }
     
      if(readValue == 1)
      {
         Serial.println("command forward" ); 
         dc.driveForward(250);
      }

      if(readValue == 2)
      {
         Serial.println("command backward" ); 
         dc.driveBackward(250);
      }
      if(readValue == 3)
      {
         Serial.println("command turn right" ); 
         dc.turnRight(180);
      }
      if(readValue == 4)
      {
         Serial.println("command turn left" ); 
         dc.turnLeft(180);
      }
      if(readValue == 5)
      {
         Serial.println("command curve right" ); 
         dc.driveCurveRight(180);
      }
      if(readValue == 6)
      {
         Serial.println("command curve left" ); 
         dc.driveCurveLeft(180);
      }
}

void loop() 
{
  // put your main code here, to run repeatedly:
  delay(10);
}
