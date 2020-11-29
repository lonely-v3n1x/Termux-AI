import subprocess as sp
from subprocess import run,Popen


class BaseApi():
    def __init__(self):
        self.api=\
            '/data/data/com.termux/files/usr/libexec/termux-api'
        #self.sp=sp

    def runcmd(self,cmd):
        try:
            return run(
                [cmd],stdout=sp.PIPE, stderr=sp.PIPE)
        except:
            print(f'Error with {cmd}')
            return None

    def termapi(self,typ,arg='',arg2=''):
        try:
            return run(
                [self.api,typ,arg,arg2],stdout=sp.PIPE, stderr=sp.PIPE)
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
        return self.termapi('BatteryStatus')

    #Set the screen brightness between 0 and 255 or auto
    def Brightness(self,lvl='',auto=False):
        if auto:
            return run( 
                f'{self.api} Brightness --ez auto true ',
                shell=True)
        else:
            return run(
                f'{self.api} Brightness --ei brightness {lvl} --ez auto false',shell=True
            )


if __name__ == "__main__":
    test=BaseApi()
    print(test.Brightness(lvl=15).returncode)
