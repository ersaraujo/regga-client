from utils.commom import GPIO

class LightSensor:
    def __init__(self):
        pass

    def read(self):
        GPIO.setup(4, GPIO.IN)
        if GPIO.input(4):
            return "Light Detected"
        else:
            return "No Light Detected"
