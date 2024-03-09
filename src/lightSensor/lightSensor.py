from utils.commom import GPIO, t

DO_PIN = 7

class LightSensor:
    def __init__(self):
        sLight = GPIO.setup(DO_PIN, GPIO.OUT)
        pass

    def read(self):
        while(True):
            if self.sLight == GPIO.LOW:
                return "Light Detected"
            else:
                return "No Light Detected"
            t.sleep(0.1)
