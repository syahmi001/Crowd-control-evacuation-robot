void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);

}

void loop() {
  if (Serial.available()){
    String payload = Serial.readStringUntil('\r\n');
    int cmd = payload.toInt();

    if (cmd == 1){
      digitalWrite(LED_BUILTIN, HIGH);
    }
    if (cmd == 0){
      digitalWrite(LED_BUILTIN, LOW);
    }
  }

}
