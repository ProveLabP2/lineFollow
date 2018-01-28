int rightPinOutput = 9;
int leftPinOutput = 10;
int rPiEnable = 3;
int leftPinInput = 4;
int rightPinInput = 5;

void setup() {
  pinMode(rightPinOutput, OUTPUT);
  pinMode(leftPinOutput, OUTPUT);
  
  pinMode(rPiEnable, INPUT);
  pinMode(leftPinInput, INPUT);
  pinMode(rightPinInput, INPUT);
}

// the loop function runs over and over again forever
void loop() {
  if (digitalRead(rPiEnable) == HIGH){
    if (digitalRead(leftPinInput) == HIGH){
      analogWrite(rightPinOutput, 126);
      analogWrite(leftPinOutput, 0);
    }
    else if (digitalRead(rightPinInput) == HIGH){
      analogWrite(leftPinOutput, 126);
      analogWrite(rightPinOutput, 0);
    }
    else{
      analogWrite(leftPinOutput, 126);
      analogWrite(rightPinOutput, 126);
    }
  }
  else{
    analogWrite(leftPinOutput, 0);
    analogWrite(rightPinOutput, 0);
  }
}
