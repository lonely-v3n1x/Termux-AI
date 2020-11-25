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

    table=Table()
    table.add_column('Name',style='green',no_wrap=True)
    table.add_column('Number',style='red')

    for i in data:
        table.add_row(i['name'],i['number'])

    console=Console()
    console.print(table)


'''
# come back to dis later

def json2table(data ,headers: list, rows: list ):
    table=Table()
    style['magenta','red',' green','cyan' ]
    for i in len(headers):
        table.add_column(
            headers[i],style=choice(style), no_wrap=True)

    for j in len(rows):
        for g in len(data):
            table.add_row(j)
'''
