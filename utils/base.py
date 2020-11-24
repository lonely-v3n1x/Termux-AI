import rich
import subprocess as sp
import json
import logging
from rich.console import Console

# Rich module Console init
console = Console()

# Saving errors and log to a fiel
logging.basicConfig(
    filename="termApi.log",
    filemode="a",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
)
logging.info("Running TermApi...")


class BaseApi(object):
    def __self__():
        self.sp = subprocess

    # log errors
    def log(self, msg):
        log = logging.getLogger("TermApi")
        log.error(msg)
        console.print(msg, style="bold red")

    # Method to run cmds
    def runcmd(self, cmd: list):
        return sp.run(cmd, stdout=sp.PIPE, stderr=sp.PIPE)

    def deviceInfo(self):
        try:
            return json.loads(self.runcmd(["termux-telephony-deviceinfo"]).stdout)
        except:
            self.log("Error accessing termux-telephony-deviceinfo")

    def audioInfo(self):
        try:
            return json.loads(self.runcmd(["termux-audio-info"]).stdout)
        except:
            self.log("Error acessing termux-audio-info")

    def batteryStatus(self):
        try:
            return json.loads(self.runcmd(["termux-battery-status"]).stdout)
        except:
            self.log("Error with termux-battery-status")

    def Toast(self, text, bg="black", cl="white", pos="top"):
        doc = """
        bg for background color ,cl for text color, pos for postion [top, middle, or bottom]
        """
        try:
            sp.run([f"termux-toast -b{bg} -c{cl} -g{pos} {text}"], shell=True)
        except:
            self.log("Error acessing termux-toast")


if __name__ == "__main__":
    test = deviceApi()
    if test.getData():
        print("Dgood")
    if not test.getHeadsetInfo():
        print("good")
