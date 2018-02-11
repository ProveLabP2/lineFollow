int rightPinENA = 9; //right enabler
int leftPinENA = 10; //left enabler

//Pi input pins
int rPiEnable = 3;

void setup() {
  pinMode(rightPinENA, OUTPUT);
  pinMode(leftPinENA, OUTPUT);
  
  pinMode(rPiEnable, INPUT);

  Serial.begin(9600);
}

// the loop function runs over and over again forever
float incomingData = 0.0;

void loop() {
  if (digitalRead(rPiEnable) == HIGH){
  if(Serial.available()){
    incomingData = Serial.parseFloat();
    if(incomingData < 1){
      analogWrite(leftPinENA, 255);
      analogWrite(rightPinENA, (incomingData)*255);
    }else if (incomingData > 1){
      analogWrite(leftPinENA, (2-incomingData)*255);
      analogWrite(rightPinENA, 255);
    }else if (incomingData == 1){
      analogWrite(leftPinENA, 255);
      analogWrite(rightPinENA, 255);
    }
  }
  }`
}
