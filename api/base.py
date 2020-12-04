import subprocess as sp
import shlex as shl
from subprocess import run, Popen
import os


class BaseApi:
    def __init__(self):
        self.api = f"{os.getcwd()}/bin/termapi"
        # self.sp=sp

    def runcmd(self, cmd):
        try:
            return run([cmd], stdout=sp.PIPE, stderr=sp.PIPE)
        except:
            print(f"Error with {cmd}")
            return None

    def termapi(self, typ, arg="", arg2=""):
        try:
            return run([self.api, typ, arg, arg2], stdout=sp.PIPE, stderr=sp.PIPE)
        except:
            return None
            print(f"Error with {typ}{arg}")

    # Returns info about device
    def DeviceInfo(self):
        return self.termapi("TelephonyDeviceInfo")

    # Return info about device audio but
    # will it to dected wireless connected headset
    def AudioInfo(self):
        return self.termapi("AudioInfo")

    # Return info about the battery
    def BatteryStatus(self):
        return self.termapi("BatteryStatus")

    # Set the screen brightness between 0 and 255 or auto
    def Brightness(self, lvl="", auto=False):
        if auto:
            return run(f"{self.api} Brightness --ez auto true ", shell=True)
        else:
            cmd = f"{self.api} Brightness --ei brightness {lvl} --ez     auto false"
            return run(shl.split(cmd))

    def CallLog(self):
        return self.termapi("CallLog")

    def Clipboard(self, get=True, st=False, inp=""):
        if get:
            return self.termapi("Clipboard")
        else:
            cmdC = f"echo -n {inp} |{self.api} Clipboard -e api_version 2 --ez set true"
            run(cmdC, shell=True)

    def ContactList(self):
        return self.termapi("ContactList")

    def Fingerprint(
        self, title="FingerPrint", desc="Authenticate Fingerprint", subs=""
    ):
        cmdFP = f"{self.api} Fingerprint --es title {title} --es description {desc} --es subtitle {subs}"
        return run(cmdFP, shell=True)

    def SmsList(self, typ="inbox", limit="10"):
        typs = ("all", "inbox", "sent", "draft", "outbox")
        if typ in typs:
            date = "--ez show-dates true"
            nums = "--ez show-phone-numbers true"
            cmdS = f"{self.api} SmsInbox {date} {nums} --ei offset 0 --ei limit {limit} --ei type {typs.index(typ)} "
            return run(cmdS, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)

        return None


if __name__ == "__main__":
    test = BaseApi()
    # test.Clipboard(get=False,inp='Fuck this shit')
    # print(test.Clipboard().stdout)
    # print(test.ContactList().stdout)
    # print(test.Fingerprint().stdout)
    # print(test.SmsList(typ='sent').stdout)
