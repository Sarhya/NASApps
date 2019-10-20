 #include <Servo.h>
 
 int EchoPin = 5;
 int TriggerPin = 6;
 int MotorAdelante = 11;
 int MotorAtras = 10;
 int led = 12;

 int posicion_1 = 90;
 int posicion_2 = -90;
 int i,j;
 
 Servo servo;
 
long distancia;
long tiempo;
 
void setup() {
   Serial.begin(9600);
  
  pinMode(MotorAdelante, OUTPUT);
  pinMode(MotorAtras,OUTPUT);
  pinMode(TriggerPin, OUTPUT);
  pinMode(EchoPin, INPUT);
  digitalWrite(TriggerPin,LOW);dr
  servo.attach(8);
  pinMode(led, OUTPUT);
  
  
  
}
 
void loop() {
  digitalWrite(TriggerPin, HIGH);  //se envía un pulso para activar el sensor
  delayMicroseconds(10);
  digitalWrite(TriggerPin, LOW);

  // medimos el pulso de respuesta
  tiempo = pulseIn(EchoPin, HIGH);


  // velocidad=(distancia/tiempo)
  // la velocidad del sonido es de 343m/s
  // Entonces:
  // 340 m/s*(1s/1000000 microsegundos)*(100 cm/1m)=2*distancia/tiempo
  // distancia=tiempo/59
  distancia = tiempo/59;

   Serial.print("Distancia: "); // imprime la distancia en el Monitor Serie
   Serial.print(distancia);
   Serial.println(" cm.");
   

if(distancia <= 30){
  

   
    for (i=55;i<110;i++){

        digitalWrite(led, HIGH);
        digitalWrite(MotorAdelante, HIGH);
        digitalWrite(MotorAtras , LOW);
        servo.write(i);
        delay(60);
        digitalWrite(led, LOW);
         }
      for(j=110;j>55;j--){        
      /*  delay(2000);
        servo.write(0);         
        delay(1000);
        servo.write(50);
        delay(1000);
         servo.write(0);
        delay(1000);       

     
        */
          digitalWrite(led, HIGH);
          digitalWrite(MotorAdelante, HIGH);
          digitalWrite(MotorAtras , LOW);        
          servo.write(j);
          delay(60);
          digitalWrite(led, LOW);
      
      }

        for(i=55;i<=82;i++){
      digitalWrite(led, HIGH);
      digitalWrite(MotorAdelante,HIGH);
      digitalWrite(MotorAtras,LOW);
      servo.write(i);
      delay(60);
      digitalWrite(led, LOW);
                     
  }
}
     
                      
 
  if (distancia > 30){
    //SE MUEVE HASTA QUE ENCUENTRE ALGO

      digitalWrite(led, HIGH);
      digitalWrite(MotorAdelante,HIGH);
      digitalWrite(MotorAtras,LOW);
      delay(500);
      
      digitalWrite(led, LOW);
      
      

      
         }
  
  delay(500);
}
