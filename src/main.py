# from humiditySensor import HumiditySensor       as hSensor
# # from temperatureSensor import TemperatureSensor as tSensor
# from lightSensor import LightSensor             as lSensor

# import time as t
# import websocket

# def main():
    
#     ws = websocket.WebSocket()
#     ws.connect("ws://plenty-monkeys-punch.loca.lt/ws")
#     lastlSensor = lSensor().read()
#     lasthSensor = hSensor().read()

#     while True:
#         _lsensor = lSensor().read()
#         _hsensor = hSensor().read()
#         if _lsensor != lastlSensor or _hsensor != lasthSensor:
#             ws.send(_lsensor)
#             ws.send(_hsensor)
#             lastlSensor = _lsensor
#             lasthSensor = _hsensor  
#             print("Update data")
#             t.sleep(2.)
#         # client.send(lSensor().read())

#     client.close()

# if __name__ == "__main__":
#     main()

# ---------------------------- TESTE SERIAL COMMUNICATION ----------------------------
import serial
import time as t

with serial.Serial('/dev/ttyUSB0', 115200) as arduino:
    t.sleep(0.1)
    if arduino.is_open():
        print("{} connected".format(arduino.port))
        try:
            while True:
                if arduino.in_waiting > 0:
                    print(arduino.readline().decode('utf-8'))
                    t.sleep(1)
        except KeyboardInterrupt:
            print("Exiting...")