import random
from  bank_account import BankAccount

class Person(BankAccount):
    
    """
    this class creates user with name, last name and account number
    """
    def __init__(self,name,lastName):

        super().__init__(0)  #initialise bank_account

        self._name = name
        self._lastName = lastName

    def getName(self):
        """
        rutr"""
        return self._name
    
    def getLastName(self):
        return self._lastName

    def __str__(self):
        return f"User is {self._name} {self._lastName} with account number ({self.getAccountType()}): {self.getAccountNumber()}"