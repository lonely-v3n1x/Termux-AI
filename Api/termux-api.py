import base


# api=base.devicApi()


class Api:
    def __init__(self):
        """ wanted to use inheritance but since i am from C lang i dont see any importance"""
        self.base = base.BaseApi()

    def getDataConnection(self):
        # print(res["data_state"])
        res = self.base.deviceInfo()
        if res["data_state"] == "connected":
            return True
        else:
            return False
        # print(res["data_state"])

    def getHeadsetInfo(self):
        res = self.base.audioInfo()
        # For debugging
        # print(res["WIREDHEADSET_IS_CONNECTED"])
        return res["WIREDHEADSET_IS_CONNECTED"]

    def getBatteryPercent(self):
        res = self.base.batteryStatus()
        # print(res["percentage"])
        return res["percentage"]

    def Toast(self, text="Enter Something"):
        return self.base.Toast(text)


if __name__ == "__main__":
    test = Api()
    """
    if test.getDataConnection():
        print("Dgood")
    else: print('No connection's)
    if test.getHeadsetInfo():
        print("good")
    else: print('no headset connected')
    test.Toast()
    print(test.getBatteryPercent())"""
