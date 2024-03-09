# from humiditySensor import HumiditySensor       as hSensor
# from temperatureSensor import TemperatureSensor as tSensor
# from lightSensor import LightSensor             as lSensor

# import time as t

# def main():
#     # print("Hello, World!")
#     while True:
#         # print("Light Sensor: ", lSensor().read())
#         # print("Temperature Sensor: ", tSensor().read())
#         print("Humidity Sensor: ", hSensor().read())
#         t.sleep(2.)

# if __name__ == "__main__":
#     main()

from socketConnection import SocketClient

def main():
    
    client = SocketClient('172.22.66.252', 12345)
    client.connect()
    client.send("Hello, World!")
    client.close()

if __name__ == "__main__":
    main()