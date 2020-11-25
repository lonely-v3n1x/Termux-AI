import base
from logprint import displayCallLogTerm 

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
    #takes raw json as arg
    def termCallLog(self):
        data=self.base.callLog()
        displayCallLogTerm(data)

    def Toast(self, text="Enter Something"):
        return self.base.Toast(text)


if __name__ == "__main__":
    test = Api()
    '''
    if test.getDataConnection():
        print("Dgood")
    else:
        print("No connection")
    if test.getHeadsetInfo():
        print("good")
    else:
        print("no headset connected")
    test.Toast()
    test.writcallLog() '''
    print(test.getBatteryPercent())
    test.termCallLog()
