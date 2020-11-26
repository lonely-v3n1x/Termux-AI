from base import BaseApi
from termprint import displayCallLogTable, displayContactTable

# api=base.devicApi()


class Api(BaseApi):
    def __init__(self):
        """ wanted to use inheritance but since i am from C lang i dont see any importance"""
        # self.base = base.BaseApi()

    def getDataConnection(self):
        # print(res["data_state"])
        res = self.deviceInfo()
        if res["data_state"] == "connected":
            return True
        else:
            return False
        # print(res["data_state"])

    def getHeadsetInfo(self):
        res = self.audioInfo()
        # For debugging
        # print(res["WIREDHEADSET_IS_CONNECTED"])
        return res["WIREDHEADSET_IS_CONNECTED"]

    def getBatteryPercent(self):
        res = self.batteryStatus()
        # print(res["percentage"])
        return res["percentage"]

    def writeCallLog(self):
        from json import dump

        with open("call.log", "w") as tmp:
            dump(self.callLog(), tmp)

    # return self.base.callLog()

    # Print call log in the terminal from logprint
    def disCallLog(self):
        data = self.callLog()
        displayCallLogTable(data)

    # display contact list in table form
    def disContactList(self):
        displayContactTable(self.contactList())

    def toast(self, text="Enter Something"):
        return self.Toast(text)


if __name__ == "__main__":
    '''
    test = Api()
    if test.getDataConnection():
        print("Dgood")
    else:
        print("No connection")
    if test.getHeadsetInfo():
        print("good")
    else:
        print("no headset connected")
    test.toast()
    test.writeCallLog()
    print(test.getBatteryPercent())
    test.disCallLog()
    test.disContactList()
    '''
