#include <AccelStepper.h>
#include <Canbus.h>
#include <defaults.h>
#include <global.h>
#include <mcp2515.h>
#include <mcp2515_defs.h>

#define STEPSIZE 1600

int PUL=7;
int DIR=6;
int ENA=5;

float xval;
float yval;
int buttonval;

int maxspeed;

AccelStepper stepper = AccelStepper(1, PUL, DIR); 

float changeRange(int val, int low, int high, int newLow, int newHigh){
    return (float)(val - low) * (newHigh - newLow) / (float)(high - low) + newLow;
}

void setup() {
   stepper.setEnablePin(ENA);
   maxspeed = STEPSIZE*2;
   stepper.setMaxSpeed(maxspeed);
   Serial.begin(9600); // For debug use
   Serial.println("CAN Read - Testing receival of CAN Bus message");  
   delay(1000);
  
   if(Canbus.init(CANSPEED_500))  //Initialise MCP2515 CAN controller at the specified speed
      Serial.println("CAN Init ok");
   else
      Serial.println("Can't init CAN");
    
   delay(1000);
}

void loop(){
   tCAN message;
   float steer_val = 0;
   if (mcp2515_check_message()){
      if (mcp2515_get_message(&message)){
         if(message.id == 0x69){
            Serial.print("ID: ");
            Serial.print(message.id,HEX);
            Serial.print(", ");
            Serial.print("Data: ");
            Serial.print(message.header.length,DEC);
            for(int i=0;i<message.header.length;i++) {	
               Serial.print(message.data[i],HEX);
               Serial.print(" ");
            }
            Serial.println("");
         }
      }
      steer_val = changeRange(message.data[0], 0, 255, -1.0, 1.0);
      stepper.setSpeed(steer_val*maxspeed);
   }
   stepper.runSpeed();

}
