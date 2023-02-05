import click
import csv
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

    file_path = filedialog.askopenfilename()
    print(file_path)

    th = TransactionHolder()
    with open(file_path, newline='') as csvfile:
        transact_reader = csv.reader(csvfile, delimiter=',', quotechar='|') 
        for row in transact_reader:
            th.parseRow(row)

    #th.organize()

    #track()

