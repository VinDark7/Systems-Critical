#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>
int l[2]={22,23};
int r[2]={24,25}; 
int i[2]={26,27};
int p[2]={28,29};
Adafruit_MPU6050 mpu;
    int l1=0;
    int l2=0;
    int r1=0;
    int r2=0;
    int i1=0;
    int i2=0;
    int p1=0;
    int p2=0;
    int accx1=0;
    int accy1=0;
    int accz1=0;
    
   int ind=0;
  int ring=0;
 int point=0;
int lilone=0;

void setup() {
   pinMode(l[0], INPUT_PULLUP );
   pinMode(l[1], INPUT_PULLUP );
   pinMode(r[0], INPUT_PULLUP );
   pinMode(r[1], INPUT_PULLUP );
   pinMode(i[0], INPUT_PULLUP );
   pinMode(i[1], INPUT_PULLUP );
   pinMode(p[0], INPUT_PULLUP );
   pinMode(p[1], INPUT_PULLUP );
             Serial.begin(9600);
              
  while (!Serial)
    delay(10); 

  Serial.println("Adafruit MPU6050 test!");

  
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }
  Serial.println("MPU6050 Found!");

  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
}


void loop() {
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);
  
  
      if(a.acceleration.x>9){
    accx1=1;}
    else{
      accx1=0;}
      if(a.acceleration.y>9){
    accy1=1;}
    else{
      accy1=0;}
      if(a.acceleration.z>9){
    accz1=1;}
    else{
      accz1=0;}
 l1 = digitalRead(l[0]);
 l2 = digitalRead(l[1]);
 p1 = digitalRead(p[0]);
 p2 = digitalRead(p[1]);
 i1 = digitalRead(i[0]); 
 i2 = digitalRead(i[1]);
 r1 = digitalRead(r[0]);
 r2 = digitalRead(r[1]);
     Serial.print( l1 );
     Serial.print( l2 );
     Serial.print( r1 );
     Serial.print( r2 );
     Serial.print( i1 );
     Serial.print( i2 );
     Serial.print( p1 );
     Serial.print( p2 );
     Serial.print( accx1 );
     Serial.print( accy1 );
     Serial.println( accz1 );

  
    
    delay(100);
    
    }
