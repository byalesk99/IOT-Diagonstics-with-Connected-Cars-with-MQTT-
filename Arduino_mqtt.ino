int motorPin1 = 3; // pin 2 on L293D IC
int motorPin2 = 4; // pin 7 on L293D IC
//int enablePin = 5; // pin 1 on L293D IC
int motorPin3 = 5; // pin 2 on L293D IC
int motorPin4 = 6;
int state=0;
int flag=0;  
int i;//makes sure that the serial only prints once the state
 
void setup() {
    // sets the pins as outputs:
    pinMode(motorPin1, OUTPUT);
    pinMode(motorPin2, OUTPUT);
     pinMode(motorPin3, OUTPUT);
    pinMode(motorPin4, OUTPUT);
    pinMode(7,OUTPUT);
    //digitalWrite(7,LOW);
   // pinMode(enablePin, OUTPUT);
    // sets enablePin high so that motor can turn on:
   // digitalWrite(enablePin, HIGH);
    // initialize serial communication at 9600 bits per second:
    Serial.begin(9600);
}
 
void loop() {
  while(1)
  {
  
    //if some date is sent, reads it and saves in state
    if(Serial.available() > 0){     
      state = Serial.read();   
      flag=0;
    }   
    
    // if the state is '0' the DC motor will turn off
    if (state == '0') {
        analogWrite(motorPin3, 255); // set pin 2 on L293D high
        analogWrite(motorPin4,0 );
        analogWrite(motorPin1,255); // set pin 2 on L293D low
        analogWrite(motorPin2, 0);
        //digitalWrite(13,HIGH);
        // set pin 7 on L293D low
        if(flag == 0){
          Serial.println("Motor: on");
          flag=1;
        }
    }
    // if the state is '1' the motor will turn right
    else if (state == '1') {
        digitalWrite(motorPin1, LOW); // set pin 2 on L293D low
        digitalWrite(motorPin2, LOW);
        digitalWrite(motorPin3, LOW); // set pin 2 on L293D low
        digitalWrite(motorPin4, LOW);// set pin 7 on L293D high
        digitalWrite(7,HIGH);
        delay(3000);
        if(flag == 0){
          Serial.println("Motor: off");
          digitalWrite(7,HIGH);
          delay(2000);
          digitalWrite(7,LOW);
          flag=1;
        }
    }
    // if the state is '2' the motor will turn left
    else if (state == '4') {
       analogWrite(motorPin3, 125); // set pin 2 on L293D high
        analogWrite(motorPin4,0 );
        analogWrite(motorPin1,0); // set pin 2 on L293D low
        analogWrite(motorPin2, 0);
       // digitalWrite(13,HIGH);
        if(flag == 0){
          Serial.println("Motor: left");
          flag=1;
        }
    }
     else if (state == '3') {
 analogWrite(motorPin3, 125); // set pin 2 on L293D high
        analogWrite(motorPin4,0 );
        analogWrite(motorPin1,0 ); // set pin 2 on L293D low
        analogWrite(motorPin2, 0);
        //digitalWrite(13,HIGH);
        if(flag == 0){
          Serial.println("Motor: right");
          flag=1;
        }
    }
    else if(state=='2')
    { for(i=0;i<125;i++){
      analogWrite(motorPin3, i); // set pin 2 on L293D high
        analogWrite(motorPin4,0 );
        analogWrite(motorPin1,i ); // set pin 2 on L293D low
        analogWrite(motorPin2, 0);
        //digitalWrite(13,HIGH);
        delay(30);}// set pin 7 on L293D low
        if(flag == 0){
          Serial.println("Motor: slow");
          flag=1;
        }
      }
       else if (state == '5  ') {
         analogWrite(motorPin3, 0); // set pin 2 on L293D high
        analogWrite(motorPin4,125 );
        analogWrite(motorPin1,0); // set pin 2 on L293D low
        analogWrite(motorPin2, 125);
        //digitalWrite(13,HIGH);
        if(flag == 0){
          Serial.println("Motor: reverse");
          flag=1;
        }
    }
    }
}
