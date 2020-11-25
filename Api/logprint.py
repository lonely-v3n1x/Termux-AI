from rich.console import Console
from rich.table import Table
#from json import load,loads

def displayCallLogTerm(data):
    #data= loads(data)

    table = Table()
    table.add_column('Name',style='magenta', no_wrap=True)
    table.add_column('Number',style='red')
    table.add_column("Type",style='green')
    table.add_column('Date', style='cyan')

    # loop thru data and print their respective values in table form
    for i in data:
        table.add_row(i['name'],i['phone_number'],i['type'],i['date'])
    console=Console()
    console.print(table)

