int rightPinENA = 9; //right enabler
int leftPinENA = 10; //left enabler

//Pi input pins
int rPiEnable = 3;

void setup() {
  pinMode(rightPinENA, OUTPUT);
  pinMode(leftPinENA, OUTPUT);
  
  pinMode(rPiEnable, INPUT);

  Serial.begin(115200);
}

// the loop function runs over and over again forever
float incomingData = 0.0;

void loop() {
  while(Serial.available()){
    byte b1 = Serial.read();
    int val = b1;
    Serial.println(val);
    if (digitalRead(rPiEnable) == HIGH){
      incomingData = val;
      if(incomingData == 0){
        return;
      }
      Serial.println(incomingData);
      if(incomingData < 255/2){
        analogWrite(leftPinENA, 255);
        analogWrite(rightPinENA, (incomingData-1)*255);
      }else if (incomingData > 255/2){
        analogWrite(leftPinENA, (255-incomingData)*255);
        analogWrite(rightPinENA, 255);
      }else if (incomingData == 255/2){
        analogWrite(leftPinENA, 255);
        analogWrite(rightPinENA, 255);
      }
    }
  }
}
