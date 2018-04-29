#include <SoftwareSerial.h>

SoftwareSerial mySerial(2, 3); // RX, TX

int ledPin = 13; 
unsigned long last = millis();//set timer
boolean ledState = 0;

void setup() {
  mySerial.begin(9600);
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  
  if(mySerial.available() > 1){    
    int input = mySerial.parseInt();//read serial input and convert to integer (-32,768 to 32,767)    

    if(millis() - last > 250){//if time now is 250 milliseconds greater than last time
      if(ledState == 0 && input == 1234){//if LED is off and button code is ok
          digitalWrite(ledPin, HIGH);
          ledState = 1;
      }else if(ledState == 1 && input == 1234){//if LED is on and button code is ok
          digitalWrite(ledPin, LOW);
          ledState = 0;
      }   
    
    }   
    
    mySerial.flush();//clear the serial buffer for unwanted inputs   
    last = millis();//reset timer   
  }
  delay(20);//delay little for better serial communication
 
}

