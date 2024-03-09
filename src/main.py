from humiditySensor import HumiditySensor       as hSensor
from temperatureSensor import TemperatureSensor as tSensor
from lightSensor import LightSensor             as lSensor

import time as t

def main():
    # print("Hello, World!")
    # print("Humidity Sensor: ", hSensor().read())
    # print("Temperature Sensor: ", tSensor().read())
    while True:
        print("Light Sensor: ", lSensor().read())
        t.sleep(0.5)

if __name__ == "__main__":
    main()