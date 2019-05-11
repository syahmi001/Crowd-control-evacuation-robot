#include <Servo.h>

Servo myservo;
int pos = 90;
//const int pwm1 = 2 ; //initializing pin 2 as pwm
//const int pwm2 = 3;
const int trigPin = 6;
const int echoPin = 5;
const int in_1 = 8 ;//ccw left motor
const int in_2 = 9 ;//cw left motor
const int in_3 = 10;//ccw right motor
const int in_4 = 11;//cw right motor

// defines variables for ultrasonic sensor
long duration;
int distance;

void setup() {
  
 Serial.begin(9600); //communication between arduino and raspberry pi
 myservo.attach(4);  // pin for servo
 pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
 pinMode(echoPin, INPUT); // Sets the echoPin as an Input
 //pinMode(pwm1,OUTPUT); //we have to set PWM pin as output
 //pinMode(pwm2,OUTPUT);
 pinMode(in_1,OUTPUT); //Logic pins are also set as output
 pinMode(in_2,OUTPUT);
 pinMode(in_3,OUTPUT);
 pinMode(in_4,OUTPUT);
 
}

void loop() {
  readface();
}


void distance_check(){
 // Clears the trigPin
digitalWrite(trigPin, LOW);
delayMicroseconds(2);

// Sets the trigPin on HIGH state for 10 micro seconds
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);

// Reads the echoPin, returns the sound wave travel time in microseconds
duration = pulseIn(echoPin, HIGH);

// Calculating the distance
distance= duration*0.034/2;

// Prints the distance on the Serial Monitor
Serial.print("Distance: ");
Serial.println(distance);

if (distance<= 50){
  Stop();
  readingmarker();
  }

  else{
    Forward();
    }
  
  }

  
void readingmarker(){

  if (Serial.available()){
    String payload = Serial.readStringUntil('\r\n');
    int cmd = payload.toInt();
    
    if (cmd == 0){
       stopmarker();
    }

    else if (cmd == 2){
       Backward();
       Right();
    }

    else if (cmd == 3){
       Backward();
       Left();
    }

  } 

  
  
  }

  
void stopmarker(){
  
   //stopping the motor
   digitalWrite(in_1,LOW);
   digitalWrite(in_2,LOW);
   digitalWrite(in_3,LOW);
   digitalWrite(in_4,LOW);
   //analogWrite(pwm1,1);
   //analogWrite(pwm2,1);
   
   for (pos = 90; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees 
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  
  for (pos = 180; pos >= 90; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  
  }

  
void Left(){
  digitalWrite(in_1,HIGH);
  digitalWrite(in_2,LOW);
  digitalWrite(in_3,LOW);
  digitalWrite(in_4,LOW);
  //analogWrite(pwm1,1);
  //analogWrite(pwm2,1);

  delay(2000);
  
  }
  
  
void Right(){
  digitalWrite(in_1,LOW);
  digitalWrite(in_2,LOW);
  digitalWrite(in_3,HIGH);
  digitalWrite(in_4,LOW);
  //analogWrite(pwm1,1);
  //analogWrite(pwm2,1);

  delay(2000);
  
  }
  

void Forward(){
  
  digitalWrite(in_1,LOW);
  digitalWrite(in_2,HIGH);
  digitalWrite(in_3,LOW);
  digitalWrite(in_4,HIGH);
  //analogWrite(pwm1,1);
  //analogWrite(pwm2,1);
  
  }
  

void Backward(){
  digitalWrite(in_1,HIGH);
  digitalWrite(in_2,LOW);
  digitalWrite(in_3,HIGH);
  digitalWrite(in_4,LOW);
  //analogWrite(pwm1,1);
  //analogWrite(pwm2,1);
  
  delay(1000);
  }


  
void Stop()
{
  //stopping the motor
   digitalWrite(in_1,LOW);
   digitalWrite(in_2,LOW);
   digitalWrite(in_3,LOW);
   digitalWrite(in_4,LOW);
   //analogWrite(pwm1,1);
   //analogWrite(pwm2,1);

   delay(50);
  
  }

void readface(){
    if (Serial.available()){
    String payload = Serial.readStringUntil('\r\n');
    int cmd = payload.toInt();

    while (cmd == 1){
       distance_check();
    }
    
  } 
   
  }
