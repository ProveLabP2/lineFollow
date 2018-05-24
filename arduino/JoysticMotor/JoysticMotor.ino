// ConstantSpeed.pde
// -*- mode: C++ -*-
//
// Shows how to run AccelStepper in the simplest,
// fixed speed mode with no accelerations
/// \author  Mike McCauley (mikem@airspayce.com)
// Copyright (C) 2009 Mike McCauley
// $Id: ConstantSpeed.pde,v 1.1 2011/01/05 01:51:01 mikem Exp mikem $
#define STEPSIZE 1600
#include <AccelStepper.h>
int PUL=7;
int DIR=6;
int ENA=5;

AccelStepper stepper = AccelStepper(1, PUL, DIR); 
     
void setup()
{ 
   stepper.setMaxSpeed(2*STEPSIZE);
   stepper.setSpeed(STEPSIZE);	
   //stepper.setAcceleration(800);

   //stepper.moveTo(32000);
}

void loop()
{  
   stepper.runSpeed();
}
