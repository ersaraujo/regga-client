import RPi.GPIO as GPIO

DO_PIN = 7
GPIO.setmode(GPIO.BCM)
GPIO.setup(DO_PIN, GPIO.IN)

class LightSensor:
    def __init__(self):
        # self.sLight = GPIO.setup(DO_PIN, GPIO.OUT)
        pass

    def read(self):
        self.sLight = GPIO.input(DO_PIN)
        if self.sLight == GPIO.LOW:
            return "Light Detected"
        else:
            return "No Light Detected"