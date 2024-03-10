import serial
import websocket
import time as t
import json
import re

def data_parser(data):
    data_len = len(data)
    for i in range(data_len):
        data[i] = re.search(r"'(.*?)\\", data[i]).group(1)
    return data

def update_data(data, temp):
    if data[0][0] == "T":
        t = data[0][1:]
        temp.update({"temperature": t})
    elif data[0][0] == "H":
        h = data[0][1:]
        temp.update({"humidity": h})
    elif data[0][0] == "L":
        l = data[0][1:]
        temp.update({"luminosity": l})
    elif data[0][0] == "U":
        u = data[0][1:]
        temp.update({"humidityGround": u})
    return temp

def main():
    temp = {
        "temperature": 0,
        "humidity": 0,
        "luminosity": 0,
        "humidityGround":0
    }
    updated = 0
    ws = websocket.WebSocket()
    ws.connect("ws://seminarios-server.loca.lt/ws")
    with serial.Serial('/dev/ttyACM1', 9600) as arduino:
        t.sleep(0.1)
        if arduino.isOpen():
            print("{} connected".format(arduino.port))
            try:
                while True:
                    if arduino.in_waiting > 0:
                        answer=str(arduino.readline())
                        dataList = answer.split("X")
                        data = data_parser(dataList)
                        temp = update_data(data, temp)
                        updated = updated + 1
                        if updated == 4:
                            updated = 0
                            ws.send(json.dumps(temp))
                            print(temp)


            except KeyboardInterrupt:
                ws.close()
                print("Exiting...")
    

if __name__ == "__main__":
    main()
