# from humiditySensor import HumiditySensor       as hSensor
# from temperatureSensor import TemperatureSensor as tSensor
from lightSensor import LightSensor             as lSensor

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

import websocket

def main():
    
    ws = websocket.WebSocket()
    ws.connect("ws://spicy-trams-laugh.loca.lt/ws")
    lastSensor = lSensor().read()

    while True:
        sensor = lSensor().read()
        ws.send("test communication")
        if sensor != lastSensor:
            ws.send(sensor)
            lastSensor = sensor
            print("Update data")
        # client.send(lSensor().read())

    client.close()

if __name__ == "__main__":
    main()