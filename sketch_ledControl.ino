const int ledRojo = 13; // LED rojo pin 13
const int ledVerde = 12; // LED verde pin 12

void setup() {
  Serial.begin(9600);
  pinMode(ledRojo, OUTPUT);
  pinMode(ledVerde, OUTPUT);
  digitalWrite(ledRojo, LOW);
  digitalWrite(ledVerde, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    char comando = Serial.read();
    if (comando == 'R') {
      digitalWrite(ledVerde, HIGH);
      digitalWrite(ledRojo, LOW);
    } else if (comando == 'G') {
      digitalWrite(ledVerde, LOW);
      digitalWrite(ledRojo, HIGH);
    } else {
      digitalWrite(ledVerde, LOW);
      digitalWrite(ledRojo, LOW);
    }
  }
}