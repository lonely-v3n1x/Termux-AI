import base


# api=base.devicApi()


class Api:
    def __init__(self):
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

    def Toast(self, text="Enter Something"):
        return self.base.Toast(text)


if __name__ == "__main__":
    test = Api()
    """if test.getDataConnection():
        print("Dgood")
    if test.getHeadsetInfo():
        print("good")"""
    test.Toast()
