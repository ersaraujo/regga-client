import serial

import websocket
import time as t

def main():
    ws = websocket.WebSocket()
    ws.connect("ws://plenty-monkeys-punch.loca.lt/ws")
    with serial.Serial('/dev/ttyACM1', 9600) as arduino:
        t.sleep(0.1)
        if arduino.isOpen():
            print("{} connected".format(arduino.port))
            try:
                while True:
                    if arduino.in_waiting > 0:
                        print("{}".format(arduino.readline()))
                        ws.send("{}".format(arduino.readline()))
                    
            except KeyboardInterrupt:
                ws.close()
                print("Exiting...")
    

with serial.Serial('/dev/ttyACM1', 9600) as arduino:
    t.sleep(0.1)
    if arduino.isOpen():
        print("{} connected".format(arduino.port))
        try:
            while True:
                if arduino.in_waiting > 0:
                    print("{}".format(arduino.readline()))
                
        except KeyboardInterrupt:
            print("Exiting...")