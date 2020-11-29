import subprocess as sp


class BaseApi():
    def __init__(self):
        self.api=\
            '/data/data/com.termux/files/usr/libexec/termux-api'

    def runcmd(self,cmd):
        try:
            return sp.run(
                [cmd],stdout=sp.PIPE, stderr=sp.PIPE)
        except:
            print(f'Error with {cmd}')
            return None

    def termapi(self,typ,arg=''):
        try:
            return sp.run(
                [self.api,typ,arg],stdout=sp.PIPE, stderr=sp.PIPE)
        except:
            return None
            print(f'Error with {typ}{arg}')

    #Returns info about device
    def DeviceInfo(self):
        return self.termapi('TelephonyDeviceInfo')

    #Return info about device audio but
    #will it to dected wireless connected headset
    def AudioInfo(self):
        return self.termapi('AudioInfo')

    #Return info about the battery
    def BatteryStatus(self):
        return self.termapi(BatteryStatus)


if __name__ == "__main__":
    test=BaseApi()
    print(test.AudioInfo().stdout)
