import serial

import websocket
import time as t

def main():
    ws = websocket.WebSocket()
    ws.connect("ws://young-windows-beam.loca.lt/ws")
    with serial.Serial('/dev/ttyACM1', 9600) as arduino:
        t.sleep(0.1)
        if arduino.isOpen():
            print("{} connected".format(arduino.port))
            try:
                while True:
                    if arduino.in_waiting > 0:
                        answer=str(arduino.readline())
                        dataList = answer.split("X")
                        print(dataList)
                        # print("{}".format(arduino.readline()))
                        # ws.send("{}".format(arduino.readline()))
                        # ws.send("Update data")
                    
            except KeyboardInterrupt:
                ws.close()
                print("Exiting...")
    

if __name__ == "__main__":
    main()


# tmp = {

# }

# data = json dump(tmp)
