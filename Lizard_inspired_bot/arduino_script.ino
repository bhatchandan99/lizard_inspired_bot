#include <Servo.h>

Servo front;
Servo middle;
Servo back;// create servo object to control a servo
// twelve servo objects can be created on most boards

int p = 0;    // variable to store the servo position

void setup() {
  front.attach(9);  
  middle.attach(6);
  back.attach(3);// attaches the servo on pin 9 to the servo object
}

void loop() {
 
front.write(80);
delay(200);
front.write(100);
delay (200);
  }
