import serial
import websocket
import json
import re
import tkinter as tk
import time as t

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

def update_screen(value):
    if valor == "feliz":
        canvas.itemconfig(rosto, image=feliz_img)
    elif valor == "sede":
        canvas.itemconfig(rosto, image=sede_img)
    elif valor == "chorando":
        canvas.itemconfig(rosto, image=chorando_img)

def set_skin(data):
    if data["temperature"] > 30:
        update_screen("sede")
    elif data["humidityGround"] < 500:
        update_screen("chorando")
    elif data["luminosity"] > 400:
        update_screen("chorando")
    else:
        update_screen("feliz")

def main():
    root = tk.Tk()
    root.title("Regga - v1.0")

    feliz_img = tk.PhotoImage(file="feliz.png")
    sede_img = tk.PhotoImage(file="sede.png")
    chorando_img = tk.PhotoImage(file="chorando.png")

    canvas = tk.Canvas(root, width=1280, height=720)
    rosto = canvas.create_image(640, 360, anchor=tk.CENTER, image=feliz_img)
    canvas.pack()

    temp = {
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
                    root.mainloop()
                    if arduino.in_waiting > 0:
                        answer=str(arduino.readline())
                        dataList = answer.split("X")
                        data = data_parser(dataList)
                        temp = update_data(data, temp)
                        print(temp)
                        set_skin(temp)
                        updated = updated + 1
                        if updated == 3:
                            updated = 0
                            ws.send(json.dumps(temp))

            except KeyboardInterrupt:
                ws.close()
                print("Exiting...")
    

if __name__ == "__main__":
    main()


# tmp = {

# }

# data = json dump(tmp)
