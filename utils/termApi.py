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

    def getHeadsetInfo(self):
        try:
            results = sp.run(["termux-audio-info"], stdout=sp.PIPE, stderr=sp.PIPE)

            res = json.loads(results.stdout)

            # For debugging
            # print(res["WIREDHEADSET_IS_CONNECTED"])

            return res["WIREDHEADSET_IS_CONNECTED"]

        except FileNotFoundError:
            log = logging.getLogger("TermApi")
            log.error("Errors with termux-audio-info")
            console.print("Problem with accessing termux-audio-info", style="bold red")
            exit()


if __name__ == "__main__":
    test = deviceApi()
    test.getHeadsetInfo()
