from enum import Enum
import logging

class TransactionHolder:
    def __init__(self):
        self.transactions = []

    # For Personal Capital style exports
    def parseRow(self, row):
        parsed_row= []
        # go through and put each line entry in array
        self.transactions.append(row)
        print(self.transactions)

#    def organize(self):

