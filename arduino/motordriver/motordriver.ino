#include <Stepper.h>

#define STEPSIZE 25600
int PUL=7; //define Pulse pin
int DIR=6; //define Direction pin
int ENA=5; //define Enable Pin

int count = 0;
int spinDir = -1;

void setup() {
  pinMode (PUL, OUTPUT);
  pinMode (DIR, OUTPUT);
  pinMode (ENA, OUTPUT);
  digitalWrite(DIR,LOW);
  digitalWrite(ENA,HIGH);

}

void loop() {
  
    digitalWrite(PUL,HIGH);
    delayMicroseconds(100);
    digitalWrite(PUL,LOW);
    delayMicroseconds(100);
    count += 1;
    
    if(count == STEPSIZE){
       count = -STEPSIZE;
       spinDir *= -1;
       if(spinDir == 1){
         digitalWrite(DIR, HIGH);
       }
       else{
         digitalWrite(DIR, LOW);
       }
    }
      
}
