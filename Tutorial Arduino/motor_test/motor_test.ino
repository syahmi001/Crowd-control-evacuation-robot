const int in_1 = 8 ; //ccw
const int in_2 = 9 ; //left motor
const int in_3 = 10; //ccw
const int in_4 = 11; //right motor

void setup() {
 pinMode(in_1,OUTPUT); //Logic pins are also set as output
 pinMode(in_2,OUTPUT);
 pinMode(in_3,OUTPUT);
 pinMode(in_4,OUTPUT);
}

void loop() {
  digitalWrite(in_1,HIGH);
  digitalWrite(in_2,HIGH);
  digitalWrite(in_3,HIGH );
  digitalWrite(in_4,HIGH);
  delay(1000);
  digitalWrite(in_1,LOW);
  digitalWrite(in_2,LOW);
  digitalWrite(in_3,LOW);
  digitalWrite(in_4,LOW);
  delay(3000);
    
}
