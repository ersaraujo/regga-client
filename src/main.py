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

ser = serial.Serial('/dev/ttyAMA0', 115200)

while True:
    ser.write("1")
    t.sleep(5)
    ser.write("0")
    t.sleep(5)