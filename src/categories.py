from enum import Enum

class IncomeCategory(Enum):
    SALARY = 1
    UNPLANNED = 2

class SavingsCategory(Enum):
    ROTH_401K = 1
    PRETAX_401K = 2
    POSTTAX_401K = 3
    ROTH_IRA = 4
    TRAD_IRA = 5
    HSA = 6
    TAXABLE = 7

class MonthlyCategory(Enum):
    PERSONAL = 1
    GROCERIES = 2
    RESTAURANT = 3
    HOBBIES = 4
    DONATIONS = 5
    VEHICLE = 6
    MISC_REQUIRED = 7
    GIFTS = 8
    SOCIAL = 9 
    PERSONAL_CARE = 10

class BlockCategory(Enum):
    CLOTHING = 1

