import Adafruit_DHT as dht

DHT = 4


class TemperatureSensor:
    def __init__(self) -> None:
        pass

    def read(self):
        h, t = dht.read_retry(dht.DHT22, DHT)
        return "Temperature: " + str(t) + "°C"
    
