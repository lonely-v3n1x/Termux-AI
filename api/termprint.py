from rich.console import Console
from rich.table import Table
from random import choice

# from json import load,loads


def displayCallLogTable(data):
    # data= loads(data)

    table = Table()
    table.add_column("Name", style="magenta", no_wrap=True)
    table.add_column("Number", style="red")
    table.add_column("Type", style="green")
    table.add_column("Date", style="cyan")

    # loop thru data and print their respective values in table form
    for i in data:
        table.add_row(i["name"], i["phone_number"], i["type"], i["date"])
    console = Console()
    console.print(table)


def displayContactTable(data):

    table = Table()
    table.add_column("Name", style="green", no_wrap=True)
    table.add_column("Number", style="red")

    for i in data:
        table.add_row(
            i["name"],
            i["number"],
        )

    console = Console()
    console.print(table)


""":
# come back to dis later

def json2table(data ,headers: list, rows: list ):
    table=Table()
    style['magenta','red',' green','cyan' ]
    len_h= len(headers)
    len_r= len(rows)

    if len_h==len_r:
        for i in headers:
            table.add_column(i)
        for h in range(len_h):
            for r in range(len_r):
                table,add_row(f"data['{data[r]}']  ")"""
