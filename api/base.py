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
            print(f'Error with {typ}{arg}')

    #Returns info about device
    def deviceInfo(self):
        return self.termapi('TelephonyDeviceInfo')

if __name__ == "__main__":
    test=BaseApi()
    print(test.deviceInfo().stdout)
