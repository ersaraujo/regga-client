import RPi.GPIO as GPIO

DO_PIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(DO_PIN, GPIO.IN)

class HumiditySensor:
    def __init__(self):
        pass
        
    def read(self):
        self.sHumidity = GPIO.input(DO_PIN)
        if self.sHumidity == GPIO.LOW:
            return "Sensor Detected"
        else:
            return "No Sensor Detected"