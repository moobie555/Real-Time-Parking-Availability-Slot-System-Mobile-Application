#define echoPin_1 2 // attach pin D2 Arduino to pin Echo of HC-SR04
#define trigPin_1 3 //attach pin D3 Arduino to pin Trig of HC-SR04
#define echoPin_2 10 // attach pin D2 Arduino to pin Echo of HC-SR04
#define trigPin_2 11 //attach pin D3 Arduino to pin Trig of HC-SR04
long duration_1;
int distance_1;
long duration_2;
int distance_2;
void setup() {
  pinMode(trigPin_1, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin_1, INPUT); // Sets the echoPin as an INPUT
  pinMode(trigPin_2, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin_2, INPUT); // Sets the echoPin as an INPUT
  Serial.begin(9600); // // Serial Communication is starting with 9600 of baudrate speed
}
void loop() {
  digitalWrite(trigPin_1, LOW);
  digitalWrite(trigPin_2, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin_1, HIGH);
  digitalWrite(trigPin_2, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin_1, LOW);
  digitalWrite(trigPin_2, LOW);
  duration_1 = pulseIn(echoPin_1, HIGH);
  duration_2 = pulseIn(echoPin_2, HIGH);
  distance_1 = (duration_1 * 0.034 / 2);
  distance_2 = (duration_2 * 0.034 / 2);  
  Serial.print(distance_1);
  Serial.print(",");
  Serial.println(distance_2);

}
