import subprocess as sp
import shlex as shl
from subprocess import run, Popen
import os


class BaseApi:
    def __init__(self):
        self.api = f"{os.getcwd()}/bin/termapi"
        # self.sp=sp

    def termapi(self, typ):
        try:
            return run([self.api, typ], stdout=sp.PIPE, stderr=sp.PIPE)
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
            #cmdC = f"echo -n {inp} |"
            cmdC=f"{self.api} Clipboard -e api_version 2 --ez set true"
            # Return bytes
            run(cmdC, shell=True,input=inp.encode())

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
            cmd_list = f"{self.api} SmsInbox {date} {nums} --ei offset 0 --ei limit {limit} --ei type {typs.index(typ)} "
            return run(cmd_list, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)

        return None

    def SmsSend(self,*numbers :list,text):
        for i in list(numbers):
            cmd_send=f'{self.api} SmsSend --esa recipients {i}'
            return run(cmd_send,shell=True,input=text.encode())

    def Toast(self,text,color='white',bgcolor='gray',pos='middle'):
       positions=('top', 'middle', 'bottom')
       if pos in positions:
            cmd_Toast=f'{self.api} Toast --ez short true --es text_color "{color}" --es background "{bgcolor}" --es gravity {pos}'
            return run(cmd_Toast,shell=True,input=text.encode(),stdout=sp.PIPE, stderr=sp.PIPE)
       else:
           return None

    def Volume(self,size='7',stream='music',st=False):
        streams=('alarm', 'music', 'notificatio', 'ring', 'system', 'call')
        if stream in streams and st==True:
            cmd_vol=f'{self.api} Volume -a set-volume --es stream {stream} --ei volume {size}'
            return run(cmd_vol,shell=True,stdout=sp.PIPE, stderr=sp.PIPE)
        elif st==False:
            cmd_vol=f'{self.api} Volume '
            return run(cmd_vol,shell=True,stdout=sp.PIPE, stderr=sp.PIPE)
        else:
            return None

if __name__ == "__main__":
    test = BaseApi()
    # test.Clipboard(get=False,inp='Fuck this shit')
    # print(test.Clipboard())
    # print(test.ContactList().stdout)
    # print(test.Fingerprint().stdout)
    # print(test.SmsList(typ='sent').stdout)
    # print(test.SmsSend(592,text='No'))
    #test.Volume('14','music',st=True)
    #print(test.Volume(st=False))
    print(test.Toast(text='hi',color='#FF0000',bgcolor='#2f706b').returncode)

