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

def update_data(data):
    if data[0][0] == "T":
        t = data[0][1:]
    elif data[0][0] == "H":
        h = data[0][1:]
    elif data[0][0] == "L":
        l = data[0][1:]
    elif data[0][0] == "U":
        u = data[0][1:]
    
    temp = {
        "temperature": t,
        "humidity": h,
        "luminosity": l,
        "humidityGround": u
    }
    return temp

def main():
    ws = websocket.WebSocket()
    # ws.connect("ws://young-windows-beam.loca.lt/ws")
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
                        temp = update_data(data)
                        # temp = {
                        #     "temperature": data[0],
                        #     "humidity": data[1],
                        #     "luminosity": data[2],
                        #     "humidityGround": data[3]
                        # }
                        print(temp)
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
