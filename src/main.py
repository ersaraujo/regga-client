from humiditySensor import HumiditySensor       as hSensor
# from temperatureSensor import TemperatureSensor as tSensor
from lightSensor import LightSensor             as lSensor

import time as t

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
    ws.connect("ws://plenty-monkeys-punch/ws")
    lastlSensor = lSensor().read()
    lasthSensor = hSensor().read()

    while True:
        _lsensor = lSensor().read()
        _hsensor = hSensor().read()
        if _lsensor != lastSensor or _hsensor != lastSensor:
            ws.send(_lsensor)
            ws.send(_hsensor)
            lastSensor = sensor
            print("Update data")
            t.sleep(2.)
        # client.send(lSensor().read())

    client.close()

if __name__ == "__main__":
    main()