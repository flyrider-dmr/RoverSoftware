/* The DISCOUNT MARS ROVER PROJECT
 * DriveControl  header file  
 * defines a class for basic driving commands
 * (c) Stefan Hager 2019
 */
 

#ifndef _DRIVECONTROL_H_

#include "motor.h"

#define _DRIVECONTROL_H_
 
 class DriveControl
 {
    
   public:
     DriveControl();
     // All drive commands issue a new action to be started.
     // The action will last until the stop command or a new 
     // drive command is issued.
     void driveBackward(int _speed);     
     void driveForward(int _speed);  
     void turnRight(int _speed);
     void turnLeft(int _speed);

     void driveCurveRight(int _speed);
     void driveCurveLeft(int _speed);
     void stop();
 };
 
 #endif
