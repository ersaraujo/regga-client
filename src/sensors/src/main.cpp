#include <Arduino.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>

#define DHTPIN A2

int LDR   = A0;
int SHUM  = A1;

DHT_Unified dht(DHTPIN, DHT22);
uint32_t delayMS;

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(LDR, INPUT);
  pinMode(SHUM, INPUT);

  dht.begin();
  sensor_t sensor;
  dht.temperature().getSensor(&sensor);
  
  delayMS = sensor.min_delay / 1000;
  Serial.begin(9600);
}

void loop() {
  while(1){
    delay(delayMS);
    sensors_event_t event;
    dht.temperature().getEvent(&event);
    if (isnan(event.temperature)) {
      Serial.println(F("Error reading temperature!"));
    } else {
      Serial.print(F("T"));
      Serial.println(event.temperature);
    }
    dht.humidity().getEvent(&event);
    if (isnan(event.relative_humidity)) {
      Serial.println(F("Error reading humidity!"));
    } else {
      Serial.print(F("H"));
      Serial.println(event.relative_humidity);
    }
    Serial.print("L");
    Serial.println(analogRead(LDR));
    Serial.print("U");
    Serial.println(analogRead(SHUM));
  }
}