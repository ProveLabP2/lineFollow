/****************************************************************************
CAN Read Demo for the SparkFun CAN Bus Shield. 

Written by Stephen McCoy. 
Original tutorial available here: http://www.instructables.com/id/CAN-Bus-Sniffing-and-Broadcasting-with-Arduino
Used with permission 2016. License CC By SA. 

Distributed as-is; no warranty is given.
*************************************************************************/
#include <Canbus.h>
#include <defaults.h>
#include <global.h>
#include <mcp2515.h>
#include <mcp2515_defs.h>

#define STEPSIZE 25000

int PUL=7; //define Pulse pin
int DIR=6; //define Direction pin
int ENA=5; //define Enable Pin

int count = 0;
int spinDir = 1;
int on = 0;
//********************************Setup Loop*********************************//

void setup() {
  pinMode (PUL, OUTPUT);
  pinMode (DIR, OUTPUT);
  pinMode (ENA, OUTPUT);
  digitalWrite(DIR,HIGH);
  digitalWrite(ENA,HIGH);

  Serial.begin(9600); // For debug use
  Serial.println("CAN Read - Testing receival of CAN Bus message");  
  delay(1000);
  
  if(Canbus.init(CANSPEED_500))  //Initialise MCP2515 CAN controller at the specified speed
    Serial.println("CAN Init ok");
  else
    Serial.println("Can't init CAN");
    
  delay(1000);
}

//********************************Main Loop*********************************//

void loop(){

  tCAN message;
if (mcp2515_check_message()) 
	{
    if (mcp2515_get_message(&message)) 
	{
        //if(message.id == 0x620 and message.data[2] == 0xFF)  //uncomment when you want to filter
             //{
               
               Serial.print("ID: ");
               Serial.print(message.id,HEX);
               Serial.print(", ");
               Serial.print("Data: ");
               Serial.print(message.header.length,DEC);
               for(int i=0;i<message.header.length;i++) 
                {	
                  Serial.print(message.data[i],HEX);
                  Serial.print(" ");
                }
               Serial.println("");
             //}
               if(message.data[0] == 0xAA){
                  on = 1;
               }
               else if (message.data[0] == 0xBB){
                  on = 0;
               }
               Serial.println(on);
           }}
    if(on == 1){
       digitalWrite(PUL, HIGH);
       delayMicroseconds(20);
       digitalWrite(PUL,LOW);
       delayMicroseconds(10);
    }
}
