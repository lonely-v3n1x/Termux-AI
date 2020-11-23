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


class deviceApi(object):
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

    def Data(self):
        try:
            getData = self.runcmd(["termux-telephony-deviceinfo"])
            res = json.loads(getData.stdout)
            # print(res["data_state"])

            if res["data_state"] == "connected":
                return True
            else:
                return False
        except:
            self.log("Error accessing termux-telephony-deviceinfo")

    def getHeadsetInfo(self):
        try:
            headsetapi = self.runcmd(["termux-audio-info"])
            res = json.loads(headsetapi.stdout)
            # For debugging
            # print(res["WIREDHEADSET_IS_CONNECTED"])

            return res["WIREDHEADSET_IS_CONNECTED"]
        except FileNotFoundError:
            self.log("Errorf accessing termux-audio-info")


if __name__ == "__main__":
    test = deviceApi()
    if test.Data():
        print("Dgood")
    if test.getHeadsetInfo():
        print("good")
