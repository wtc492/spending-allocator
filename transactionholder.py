import click
from enum import Enum
import logging

class TransactionHolder:
    def __init__(self):
        self.transactions = []

    # For Personal Capital style exports
    def parseRow(self, row):
        click.echo(row)
        if click.confirm('Do you have any changes?', default=False):
            row.append(True)
            # logic for making edits

        self.transactions.append(row)

    def printTransactions(self):
        for row in self.transactions:
            click.echo(row)

#    def organize(self):

