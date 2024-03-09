# from humiditySensor import HumiditySensor       as hSensor
# from temperatureSensor import TemperatureSensor as tSensor
# from lightSensor import LightSensor             as lSensor

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


import socket

def main():
    # Configurar o servidor
    host = 'localhost'  # ou '0.0.0.0' para aceitar conexões de qualquer IP
    port = 12345        # Número da porta
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Aguardando conexão do cliente...")
    conn, addr = server_socket.accept()
    print("Conexão estabelecida com", addr)

    # Enviar dados para o cliente
    data_to_send = "Hello, client!"
    conn.sendall(data_to_send.encode())

    # Fechar a conexão
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    main()