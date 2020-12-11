#include <Servo.h> 


#define servo1Pin 2
#define servo2Pin 3
#define servo3Pin 4
#define servo4Pin 5
#define servo5Pin 6
#define servo6Pin 7

byte packetStart = 254;
byte packetEnd = 255; 
byte data[] = {0,0,0,0,0,0,0,0};
int cur =0;
bool NewData = false;
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;

void setup() {
  // put your setup code here, to run once:
Serial.begin(2000000);
Serial.println("Serial Started...");
servo1.attach(servo1Pin);
servo2.attach(servo2Pin);
servo3.attach(servo3Pin);
servo4.attach(servo4Pin);
servo5.attach(servo5Pin);
servo6.attach(servo6Pin);
//pinMode(LED_BUILTIN,OUTPUT);
}
byte input[6] ={0};
void loop() {
  // put your main code here, to run repeatedly:
if(Serial.available() >0) {
  Serial.readBytes(input,1);
  if (input[0] == packetStart) {
    cur = 0;
    NewData = true;
    while (input[0] !=packetEnd) {
      if(Serial.available()>0) {
      Serial.readBytes(input,1);
      data[cur] = input[0];
      cur = cur +1;
      }
    }
  }
    
}
if(NewData==true) {
  //digitalWrite(LED_BUILTIN,HIGH);
  servo1.write(data[0]);
  servo2.write(data[1]);
  servo3.write(data[2]);
  servo4.write(data[3]);
  servo5.write(data[4]);
  servo6.write(data[5]);
  delay(500);
  /*digitalWrite(LED_BUILTIN,LOW);
  NewData=false;*/
}

}
