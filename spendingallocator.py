import click
import tkinter as tk
from tkinter import filedialog

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')

def track(count, name):
    """print("Enter your trkansaction")
    with open_file('../testdir/2022-07-01 thru 2022-07-31 transactions.csv')
        :L"""

    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    print(file_path)

    #track()

