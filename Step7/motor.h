/* The DISCOUNT MARS ROVER PROJECT
 * motor header file  
 * defines a class to control a DC Motor via L298D H-Bridge
 * (c) Stefan Hager 2019
 */
 
 #ifndef _MOTOR_H_
 #define _MOTOR_H_
 
 class Motor
 {
   private:
    int PWMPort, forwardPort, backwardPort, speed;  
   public:
    Motor (int _PWMport, int _forward, int _backward); // constructor
    void setSpeed (int _speed);
    void driveForward();
    void driveBackward();
    void stop();
 };
 
 #endif
