import click
import csv
import time
import tkinter as tk
from tkinter import filedialog
from transactionholder import *

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')

def track(count, name):
    """print("Enter your transaction")
    with open_file('../testdir/2022-07-01 thru 2022-07-31 transactions.csv')
        :L"""

    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    click.echo('Choose your monthly transaction file')

    # consider using click File Arguments - not sure if it's appropriate
    file_path = filedialog.askopenfilename()
    time.sleep(0.5)
    print(file_path)

    th = TransactionHolder()
    # get # of rows so that each confirmation can be printed with x/y so user knows how far they are
    with open(file_path, newline='') as csvfile:
        transact_reader = csv.reader(csvfile, delimiter=',', quotechar='|') 
        for count, row in enumerate(transact_reader):
            th.parseRow(count, row)

    th.printTransactions()
    #th.organize()

    #track()

