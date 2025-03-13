import random
class BankAccount:
    """
    This class manages the bank account, including balance, deposits, withdrawals, and account number.
    """

    def __init__(self, balance):

        self._balance = balance
        self._accountNumber = 0
        self.getAccountType =None

    def deposit(self,amount):
        if amount >0:

            self._balance+=amount
        
        else:
            raise ValueError("Amount cannot be negative")
        
    def withdraw(self,amount):

        if amount<=self._balance:
            self._balance-=amount
            return {"balance":self._balance,"amount":f"amount withdrawn: {amount}"}
        else:
            raise ValueError(f"{amount} exceed available balance of: R{self._balance}")
            
    
    def getBalance(self):
        return self._balance
    
    def createAccountNumber(self):

        """
        this generates account number
        """
        self._accountNumber = random.randint(1000000,1000000000)
    
    def getAccountNumber(self):

        """
        Returns the account number. If not set, generates a new one.
        """
        if self._accountNumber == 0:
            self.createAccountNumber()  # Ensure account number is created if not yet set
        return self._accountNumber
    
    
    def setAccountType(self,type):
        self._accountType = type
    
    
    def getAccountType(self):
        
        return self._accountType
    
    def __str__(self):
        return f"Account Number({self.getAccountType()}): {self.getAccountNumber()}, Balance: {self.getBalance()}"
    
    

        
