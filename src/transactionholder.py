import click
from enum import Enum
import logging

class TransactionHolder:
    def __init__(self):
        self.transactions = []
        self.headers = []

    # For Personal Capital style exports
    def parseRow(self, count, row):
        click.echo(count, ': ', row)
        if count == 0:
            self.headers.append('Line')
            for col in row:
                self.headers.append(col)
            self.headers.append('isChanged')
            click.echo(row)
        elif click.confirm('Do you have any changes?', default=False):
            # TODO - put it in a do while loop?
            while changeColValue(row) == True:
                row.append(True)
            # logic for making edits

        self.transactions.append(row)

    def changeColValue(self, row):
        col_to_change = click.prompt('Which column do you want to change?')

    def printTransactions(self):
        for row in self.transactions:
            click.echo(row)

#    def organize(self):

