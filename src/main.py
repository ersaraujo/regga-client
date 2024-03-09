from humiditySensor import HumiditySensor       as hSensor
from temperatureSensor import TemperatureSensor as tSensor
from lightSensor import LightSensor             as lSensor

def main():
    # print("Hello, World!")
    # print("Humidity Sensor: ", hSensor().read())
    # print("Temperature Sensor: ", tSensor().read())
    print("Light Sensor: ", lSensor().read())

if __name__ == "__main__":
    main()