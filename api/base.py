import rich
import subprocess as sp
from json import loads
import logging
from rich.console import Console
from rich.logging import RichHandler

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

"""'logging.basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)]
)"""


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
        try:
            return sp.run(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
            # self.log(f"Success {cmd}")
        except:
            self.log(f"Error accessing {cmd}")

    def deviceInfo(self):
        return loads(self.runcmd(["termux-telephony-deviceinfo"]).stdout)

    def audioInfo(self):
        return loads(self.runcmd(["termux-audio-info"]).stdout)

    def batteryStatus(self):
        return loads(self.runcmd(["termux-battery-status"]).stdout)

    def callLog(self):
        return loads(self.runcmd(["termux-call-log"]).stdout)

    def contactList(self):
        return loads(self.runcmd(["termux-contact-list"]).stdout)

    def Toast(self, text, bg="black", cl="white", pos="top"):
        doc = """
        bg for background color ,cl for text color, pos for postion [top, middle, or bottom]
        """
        try:
            sp.run([f"termux-toast -b{bg} -c{cl} -g{pos} {text}"], shell=True)
        except:
            self.log("Error acessing termux-toast")


if __name__ == "__main__":
    test = BaseApi()
    if test.getData():
        print("Dgood")
    if not test.getHeadsetInfo():
        print("good")
