// ConstantSpeed.pde
// -*- mode: C++ -*-
//
// Shows how to run AccelStepper in the simplest,
// fixed speed mode with no accelerations
/// \author  Mike McCauley (mikem@airspayce.com)
// Copyright (C) 2009 Mike McCauley
// $Id: ConstantSpeed.pde,v 1.1 2011/01/05 01:51:01 mikem Exp mikem $

#include <AccelStepper.h>

#define STEPSIZE 1600

const int aPinY = A0;
const int aPinX = A1;
int buttonPin = 2;

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

void setup()
{  
   stepper.setEnablePin(ENA);
   maxspeed = STEPSIZE*2;
   stepper.setMaxSpeed(maxspeed);
   
}

void loop()
{  
   stepper.runSpeed();
   xval = analogRead(aPinX);
   xval = changeRange(float(xval), 0.0, 1023.0, -1.0, 1.0);
   yval = analogRead(aPinY);
   yval = changeRange(float(yval), 0.0, 1023.0, -1.0, 1.0);
   buttonval = digitalRead(buttonPin);

   stepper.setSpeed(maxspeed*yval);
}
