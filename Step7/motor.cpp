/* The DISCOUNT MARS ROVER PROJECT
 * motor implementation file  
 * implements a class to control a DC Motor via L298D H-Bridge
 * (c) Stefan Hager 2019
 */

#include "motor.h"
#include "Arduino.h"

Motor::Motor (int _PWMport, int _forward, int _backward) 
{
  PWMPort = _PWMport;
  forwardPort = _forward; 
  backwardPort = _backward; 
  speed = 0;

  pinMode(PWMPort, OUTPUT);
  pinMode(forwardPort, OUTPUT);
  pinMode(backwardPort, OUTPUT);
}

void Motor::setSpeed (int _speed)
{
  speed = _speed;
}

void Motor::driveForward()
{
  digitalWrite(forwardPort, HIGH);
  digitalWrite(backwardPort, LOW);
  analogWrite(PWMPort, speed); // Send PWM signal to L298N Enable pin
}

void Motor::driveBackward()
{
  digitalWrite(forwardPort, LOW);
  digitalWrite(backwardPort, HIGH);
  analogWrite(PWMPort, speed); // Send PWM signal to L298N Enable pin
}

void Motor::stop()
{ 
  analogWrite(PWMPort, 0); // Send speed 0 to PWM signal pin  
}
