#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position

void setup() {
  Serial.begin(9600);
  myservo.attach(4);  // attaches the servo on pin 9 to the servo object
}

void loop() {
myservo.write(90);
  
}
  /*if (Serial.available()){
    String payload = Serial.readStringUntil('\r\n');
    int cmd = payload.toInt();

    if (cmd == 1){
       for (pos = 90; pos <= 135; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);
    
    // waits 15ms for the servo to reach the position
  }
  for (pos = 135; pos >= 90; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
    }

   else if (cmd == 0){
   myservo.write(45);              // tell servo to go to position in variable 'pos'
   delay(15); 
   } 

  }
}*/


/*void loop() {
  for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
}*/
