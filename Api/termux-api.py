import base
from logprint import displayCallLogTable,displayContactTable

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

    def writeCallLog(self):
        from json import dump
        with open('call.log','w') as tmp:
            dump(self.base.callLog(),tmp)
       #return self.base.callLog()

    #Print call log in the terminal from logprint
    def disCallLog(self):
        data=self.base.callLog()
        displayCallLogTable(data)

    #display contact list in table form
    def disContactList(self):
        displayContactTable(self.base.contactList())

    def Toast(self, text="Enter Something"):
        return self.base.Toast(text)


if __name__ == "__main__":
    test = Api()
    
    if test.getDataConnection():
        print("Dgood")
    else:
        print("No connection")
    if test.getHeadsetInfo():
        print("good")
    else:
        print("no headset connected")
    test.Toast()
    test.writeCallLog()
    #print(test.getBatteryPercent())
    test.disCallLog()
    test.disContactList()
