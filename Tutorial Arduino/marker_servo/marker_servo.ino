#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position

const int in_1 = 8 ;
const int in_2 = 9 ;
const int in_3 = 10;
const int in_4 = 11;

char data; //initialize state variable
void setup() 
{
 Serial.begin(9600);
 pinMode(in_1,OUTPUT); //Logic pins are also set as output
 pinMode(in_2,OUTPUT);
 pinMode(in_3,OUTPUT);
 pinMode(in_4,OUTPUT);
 myservo.attach(4);  // attaches the servo on pin 9 to the servo object
 }

void loop() {
  // put your main code here, to run repeatedly:
 if(Serial.available()>0)
   {     
      data= Serial.read(); // reading the data received from the bluetooth module
      switch(data)
      {
        case 'w': 
        digitalWrite(in_1,LOW);
        digitalWrite(in_2,HIGH);
        digitalWrite(in_3,LOW);
        digitalWrite(in_4,HIGH);
        break;
        
        case 's': 
        digitalWrite(in_1,HIGH);
        digitalWrite(in_2,LOW);
        digitalWrite(in_3,HIGH);
        digitalWrite(in_4,LOW);
        break;
        
        case 'd': 
        digitalWrite(in_1,HIGH); 
        digitalWrite(in_2,LOW); 
        digitalWrite(in_3,LOW); 
        digitalWrite(in_4,LOW);
        break;
         
        case 'a': 
        digitalWrite(in_1,LOW); 
        digitalWrite(in_2,LOW); 
        digitalWrite(in_3,HIGH); 
        digitalWrite(in_4,LOW);
        break;
        
        case'g':
        digitalWrite(in_1,LOW); 
        digitalWrite(in_2,LOW); 
        digitalWrite(in_3,LOW); 
        digitalWrite(in_4,LOW);
        break;

        case'z':
        servo();
        default :
        break;
      }
      
   }
delay(50);

}


void servo(){
for (pos = 0; pos <= 90; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 90; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  }

