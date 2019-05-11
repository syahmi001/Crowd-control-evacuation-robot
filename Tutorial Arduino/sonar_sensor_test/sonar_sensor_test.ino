/*
* Ultrasonic Sensor HC-SR04 and Arduino Tutorial
*
* by Dejan Nedelkovski,
* www.HowToMechatronics.com
*
*/

/*// defines pins numbers
const int trigPin = 6;
const int echoPin = 5;

// defines variables
long duration;
int distance;

void setup() {
pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
pinMode(echoPin, INPUT); // Sets the echoPin as an Input
Serial.begin(9600); // Starts the serial communication
}

void loop() {
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

if (distance<15){*/

const int trigPin = 6;
const int echoPin = 5;
const int in_1 = 8 ;
const int in_2 = 9 ;
const int in_3 = 10;
const int in_4 = 11;

// defines variables
long duration;
int distance;

void setup() {
  
 Serial.begin(9600);
 pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
 pinMode(echoPin, INPUT); // Sets the echoPin as an Input
 pinMode(in_1,OUTPUT); //Logic pins are also set as output
 pinMode(in_2,OUTPUT);
 pinMode(in_3,OUTPUT);
 pinMode(in_4,OUTPUT);
 
}

void loop() {
  distance_check();
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

if (distance<= 15){
  Stop();
  }

  else{
    Forward();
    }
  
  }

void Forward(){
  
  digitalWrite(in_1,HIGH);
  digitalWrite(in_2,LOW);
  digitalWrite(in_3,HIGH);
  digitalWrite(in_4,LOW);

  
  }

  
void Stop()
{
  //stopping the motor
   digitalWrite(in_1,LOW);
   digitalWrite(in_2,LOW);
   digitalWrite(in_3,LOW);
   digitalWrite(in_4,LOW);

   delay(2000);
  
  }


