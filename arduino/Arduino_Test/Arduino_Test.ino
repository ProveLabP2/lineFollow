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

  /*digitalWrite(rPinOne, HIGH);
  digitalWrite(rPinTwo, LOW);
  digitalWrite(lPinOne, HIGH);
  digitalWrite(lPinTwo, LOW);*/

  Serial.begin(9600);
}

void loop(){
  forward();
  delay(250);
  /*right();
  delay(250);
  left();
  delay(250);*/
}

void forward(){
  digitalWrite(rPinOne, HIGH);
  digitalWrite(rPinTwo, LOW);
  digitalWrite(lPinOne, HIGH);
  digitalWrite(lPinTwo, LOW);

  digitalWrite(rightPinENA, HIGH);
  digitalWrite(leftPinENA, HIGH);
  delay(750);
  analogWrite(rightPinENA, 0);
  analogWrite(leftPinENA, 0);
}
/*void right(){
  digitalWrite(rPinOne, HIGH);
  digitalWrite(rPinTwo, LOW);
  digitalWrite(lPinOne, HIGH);
  digitalWrite(lPinTwo, LOW);

  analogWrite(rightPinENA, 0);
  analogWrite(leftPinENA, 126);
  delay(750);
  analogWrite(rightPinENA, 0);
  analogWrite(leftPinENA, 0);
}

void left(){
  digitalWrite(rPinOne, HIGH);
  digitalWrite(rPinTwo, LOW);
  digitalWrite(lPinOne, HIGH);
  digitalWrite(lPinTwo, LOW);

  analogWrite(rightPinENA, 126);
  analogWrite(leftPinENA, 0);
  delay(750);
  analogWrite(rightPinENA, 0);
  analogWrite(leftPinENA, 0);
}
*/
