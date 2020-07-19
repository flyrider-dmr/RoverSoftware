/* The DISCOUNT MARS ROVER PROJECT
 * DriveControl  implementation file  
 * defines a class for basic driving commands
 * (c) Stefan Hager 2019
 */

#include "DriveControl.h"
#include "motor.h"
#include "Arduino.h"

  Motor  m1 (7,28,29);
  Motor  m2 (4,23,22);
  Motor  m3 (6,31,30);
  Motor  m4 (3,25,24);
  Motor  m5 (5,33,32);
  Motor  m6 (2,27,26);
    

void DriveControl::driveForward(int _speed)
{
  // set speed
  m1.setSpeed(_speed);
  m2.setSpeed(_speed);
  m3.setSpeed(_speed);
  m4.setSpeed(_speed);
  m5.setSpeed(_speed);
  m6.setSpeed(_speed);
  // and go...
  m1.driveForward();
  m2.driveForward();
  m3.driveForward();
  m4.driveForward();
  m5.driveForward();
  m6.driveForward();
  
}

void DriveControl::driveBackward(int _speed)
{
 // set speed
  m1.setSpeed(_speed);
  m2.setSpeed(_speed);
  m3.setSpeed(_speed);
  m4.setSpeed(_speed);
  m5.setSpeed(_speed);
  m6.setSpeed(_speed);
  // and go...
  m1.driveBackward();
  m2.driveBackward();
  m3.driveBackward();
  m4.driveBackward();
  m5.driveBackward();
  m6.driveBackward();
}
void DriveControl::turnRight(int _speed)
{
  // set speed
  m1.setSpeed(_speed);
  m2.setSpeed(_speed);
  m3.setSpeed(_speed);
  m4.setSpeed(_speed);
  m5.setSpeed(_speed);
  m6.setSpeed(_speed);
  // and go...
  m1.driveForward();
  m2.driveBackward();
  m3.driveForward();
  m4.driveBackward();
  m5.driveForward();
  m6.driveBackward();
}

void DriveControl::turnLeft(int _speed)
{
// set speed
  m1.setSpeed(_speed );
  m2.setSpeed(_speed);
  m3.setSpeed(_speed );
  m4.setSpeed(_speed);
  m5.setSpeed(_speed );
  m6.setSpeed(_speed);
  // and go...
  m1.driveBackward();
  m2.driveForward();
  m3.driveBackward();
  m4.driveForward();
  m5.driveBackward();
  m6.driveForward();
}

DriveControl::DriveControl()  {}

void DriveControl::driveCurveRight(int _speed)
{
  // set different speed on both sides plus minus 25 %
  int outerturnspeed = _speed + _speed * 0.25;
  int innerturnspeed = _speed - _speed * 0.25;
  
  // set speed
  m1.setSpeed(innerturnspeed );
  m3.setSpeed(innerturnspeed);
  m5.setSpeed(innerturnspeed );
  
  m2.setSpeed(outerturnspeed);
  m4.setSpeed(outerturnspeed );
  m6.setSpeed(outerturnspeed);

  // go ...
  m1.driveForward();
  m2.driveForward();
  m3.driveForward();
  m4.driveForward();
  m5.driveForward();
  m6.driveForward();
}

void DriveControl::driveCurveLeft(int _speed)
{
  // set different speed on both sides plus minus 25 %
  int innerturnspeed = _speed - _speed * 0.25;
  int outerturnspeed = _speed + _speed * 0.25;

  // set speed
  m1.setSpeed(outerturnspeed);
  m3.setSpeed(outerturnspeed);
  m5.setSpeed(outerturnspeed);
  
  m2.setSpeed(innerturnspeed);
  m4.setSpeed(innerturnspeed);
  m6.setSpeed(innerturnspeed);

    // go ...
  m1.driveForward();
  m2.driveForward();
  m3.driveForward();
  m4.driveForward();
  m5.driveForward();
  m6.driveForward();
}

void DriveControl::stop()
{
  // Easy ... stop all motors
  m1.stop();
  m2.stop();
  m3.stop();
  m4.stop();
  m5.stop();
  m6.stop();
}
