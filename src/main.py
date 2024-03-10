import serial
import websocket
import json
import re
import tkinter as tk
import time as t
import datetime

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

def update_screen(value, canvas):
    feliz_img = tk.PhotoImage(file="feliz.png")
    sede_img = tk.PhotoImage(file="sede.png")
    chorando_img = tk.PhotoImage(file="chorando.png")
    if value == "feliz":
        rosto = canvas.create_image(640, 360, anchor=tk.CENTER, image=feliz_img)
        canvas.itemconfig(rosto, image=feliz_img)
    elif value == "sede":
        rosto = canvas.create_image(640, 360, anchor=tk.CENTER, image=feliz_img)
        canvas.itemconfig(rosto, image=sede_img)
    elif value == "chorando":
        rosto = canvas.create_image(640, 360, anchor=tk.CENTER, image=feliz_img)
        canvas.itemconfig(rosto, image=chorando_img)

def set_skin(data, canvas):

    temperature = data["temperature"]
    humidity_ground = data["humidityGround"]
    luminosity = data["luminosity"]

    if float(temperature) > 30.:
        update_screen("sede", canvas)
    elif int(humidity_ground) < 500:
        update_screen("chorando",canvas)
    elif int(luminosity) > 400:
        update_screen("chorando", canvas)
    else:
        update_screen("feliz",canvas)

def main():
    root = tk.Tk()
    root.title("Regga - v1.0")

    canvas = tk.Canvas(root, width=1280, height=720)
    canvas.pack()

    temp = {
        "temperature_sensor_id": "500",
        "light_sensor_id": "500",
        "humidity_sensor_id": "500",
        "device_id": "200",
        "plant_id": "10203",
        "plant_name": "dev_plant",
        "timestamp": str(datetime.datetime.now()),
        "temperature": 0,
        "humidity": 0,
        "luminosity": 0,
        "humidityGround":0
    }
    updated = 0

    ws = websocket.WebSocket()
    ws.connect("ws://seminarios-server.loca.lt/ws")
    
    with serial.Serial('/dev/ttyACM0', 9600) as arduino:
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
                        print(temp)
                        set_skin(temp, canvas)
                        updated = updated + 1
                        if updated == 3:
                            updated = 0
                            ws.send(json.dumps(temp))
                    root.update()

            except KeyboardInterrupt:
                ws.close()
                print("Exiting...")
    

if __name__ == "__main__":
    main()
