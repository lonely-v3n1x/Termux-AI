import rich
import subprocess as sp
from rich.console import Console
import validators
try:
    from func import parse,uri_validator
except :
    print('load not found')
    quit()


# Rich module Console init
console = Console()

class BaseApi(object):
    def __self__():
        self.sp = subprocess

    # Method to run cmds
    def runcmd(self, cmd: list):
        try:
            return sp.run(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
        except:
            print(f"Error with {cmd}")
    def deviceInfo(self):
        return loads(
            self.runcmd(["termux-telephony-deviceinfo"]).stdout)

    def audioInfo(self):
        return loads(self.runcmd(["termux-audio-info"]).stdout)

    def batteryStatus(self):
        return loads(
            self.runcmd(["termux-battery-status"]).stdout)

    def brightness(self,num):
        if (num > 0 and num < 255):
            sp.run(['termux-brightness', str(num) ])
            return True
        return False

    #Use arg get=True to return json of volume data
    def volume(self,stream,vol :int):
        streams=('alarm', 'music', 
                 'notification', 'ring', 'system', 'call')
        if stream in streams:
            sp.run(['termux-volume',stream,str(vol)])
        return False

    def callLog(self):
        return loads(
            self.runcmd(["termux-call-log"]).stdout)

    def contactList(self):
        return loads(
            self.runcmd(["termux-contact-list"]).stdout)

    def url_open(self,url):
        if validators.url(url):
            sp.run([f'termux-open-url',url])
            return True
        return False

    def toast(self, text, bg="black", cl="white", pos="top"):
        doc = """
        bg for background color ,cl for text color, pos for postion [top, middle, or bottom]
        """
        try:
            sp.run(
                [f"termux-toast -b{bg} -c{cl} -g{pos} {text}"], shell=True)
        except:
            self.log("Error acessing termux-toast")


if __name__ == "__main__":
    test = BaseApi()
