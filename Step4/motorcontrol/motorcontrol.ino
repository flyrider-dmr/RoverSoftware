    /*  The DISCOUNT MARS ROVER PROJECT
     *  Motor test for DC motor
     * (c) Stefan Hager, 2019
    */
    
    #include "motor.h"
    
    const unsigned long  BAUDRATE = 9600;
    Motor motor1 (7,28,29);
    int readValue = 0;
    
    void setup() 
    {
      Serial.begin(BAUDRATE);
      Serial.println("Discount Rover motor test is ready..." );
      motor1.setSpeed(200);
    }

    void serialEvent()
    {  
      readValue   = Serial.parseInt();
      
      if(readValue == 3)
      {
         Serial.println("command stop" ); 
         motor1.stop();
      }
      
      if(readValue == 1)
      {
         Serial.println("command forward" ); 
         motor1.driveForward();
      }

      if(readValue == 2)
      {
         Serial.println("command backward" ); 
         motor1.driveBackward();
      }
      
    }
    
    void loop() 
    {
      delay(10);
    }
