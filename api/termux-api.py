from base import BaseApi
from termprint import displayCallLogTable, displayContactTable
from ujson import dump, loads

# api=base.devicApi()


class Api(BaseApi):
    def __init__(self):
        # self.base = base.BaseApi()
        pass

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

    def getClipboard(self):
        # it return's a bytes string
        return self.clipboard(get=True, st=False)

    def setClipboard(self, usr):
        # sets usr to clipboard
        self.clipboard(get=False, st=True, inp=usr)

    def setBrightness(self, num):
        self.brightness(num)

    def getVolume(self):
        return loads(self.runcmd(["termux-volume"]).stdout)

    def setVolume(self, stream, num):
        self.volume(stream, num)

    # write's call log to a file call.log
    def writeCallLog(self):
        with open("call.log", "w") as tmp:
            dump(self.callLog(), tmp)
            # return self.base.callLog()

    # Print call log in the terminal from logprint
    def disCallLog(self):
        data = self.callLog()
        displayCallLogTable(data)

    # overider url_open
    def web_open(self, url):
        self.url_open(url)

    # display contact list in table form
    def disContactList(self):
        displayContactTable(self.contactList())

    def Toast(self, text="Enter Something"):
        return self.toast(text)


if __name__ == "__main__":
    test = Api()
    """
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
    test.web_open('https://google.com')
    test.setBrightness(15)
    test.setVolume('music','5')
    print(test.getVolume())"""
    test.setClipboard("Usr\nIts Works")
    print(test.getClipboard().decode())
