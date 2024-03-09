class HumiditySensor:
    def __init__(self, humiditySensorAdapter):
        self.humiditySensorAdapter = humiditySensorAdapter

    def getHumidity(self):
        return self.humiditySensorAdapter.getHumidity()