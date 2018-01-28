int rightPinENA = 9; //right enabler
int leftPinENA = 10; //left enabler
//right pin leads
int rPinOne = 8;
int rPinTwo = 7;
//left pin leads
int lPinOne = 6;
int lPinTwo = 5;
//Pi input pins
int rPiEnable = 3;
int leftPinInput = 4;
int rightPinInput = 5;

void setup() {
  pinMode(rightPinENA, OUTPUT);
  pinMode(leftPinENA, OUTPUT);
  pinMode(rPinOne, OUTPUT);
  pinMode(rPinTwo, OUTPUT);
  pinMode(lPinOne, OUTPUT);
  pinMode(lPinTwo, OUTPUT);
  
  pinMode(rPiEnable, INPUT);
  pinMode(leftPinInput, INPUT);
  pinMode(rightPinInput, INPUT);

  digitalWrite(rPinOne, HIGH);
  digitalWrite(rPinTwo, LOW);
  digitalWrite(lPinOne, HIGH);
  digitalWrite(lPinTwo, LOW);
}

// the loop function runs over and over again forever
void loop() {
  if (digitalRead(rPiEnable) == HIGH){
    if (digitalRead(leftPinInput) == HIGH){
      analogWrite(rightPinENA, 126);
      analogWrite(leftPinENA, 0);
    }
    else if (digitalRead(rightPinInput) == HIGH){
      analogWrite(leftPinENA, 126);
      analogWrite(rightPinENA, 0);
    }
    else{
      analogWrite(leftPinENA, 126);
      analogWrite(rightPinENA,126);
    }
  }
  else{
    analogWrite(leftPinENA, 0);
    analogWrite(rightPinENA, 0);
  }
  
}
