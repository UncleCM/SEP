import ZODB, ZODB.config
import persistent
from time import strftime, localtime
from abc import ABC, abstractmethod

class Customer(persistent.Persistent):
    def __init__(self, name=""):
        self.name = name
        self.accounts = persistent.list.PersistentList()
    
    def __str__(self):
        return "Customer Name: " + self.name
    
    def addAccount(self, a):
        self.accounts.append(a)
        return a
    
    def getAccount(self, n):
        if 0 <= n < len(self.accounts):
            return self.accounts[n]
        return None

    def printStatus(self):
        print(self.__str__())
        for a in self.accounts:
            print("", end="")
            a.printStatus()

class BankTransaction():
    def __init__(self, amount, new_balance, old_balance, timestamp, ttype, recipient = None):
        self.amount = amount
        self.new_balance = new_balance
        self.old_balance = old_balance
        self.timestamp = timestamp
        self.ttype = ttype
        self.recipient = recipient
    
    def printDetail(self):
        match self.ttype:
            case "deposit":
                print("Deposit")
            case "withdrawal":
                print("Withdraw")
            case "transfer":
                print(f"Transfer to {self.recipient}")
            case "transferin":
                print(f"Transfer from {self.recipient}")
        print(f"\tAmount: {self.amount}")
        print(f"\tOld Balance: {self.old_balance}")
        print(f"\tNew Balance: {self.new_balance}")
        print(f"\tTime Stamp: {self.timestamp}")

class Account(ABC):
    def __init__(self, balance = 0.0, owner = None):
        self.balance = balance
        self.owner = owner
        self.bankTransaction = []
    
    @abstractmethod
    def __str__(self):
        raise NotImplementedError("You should probably define __str__")
    
    def deposit(self, m):
        old_balance = self.balance
        self.balance += m
        transaction = BankTransaction(m, self.balance, old_balance, strftime("%Y-%m-%d %H:%M:%S", localtime()), "deposit")
        self.bankTransaction.append(transaction)
    
    @abstractmethod
    def withdraw(self):
        raise NotImplementedError("You should probably define withdraw")
    
    @abstractmethod
    def transfer(self, m, other_acc):
        raise NotImplementedError("You should probably define transfer")
    
    def transferIn(self, m, other_acc):
        old_balance = self.balance
        self.balance += m
        transaction = BankTransaction(m, self.balance, old_balance, strftime("%Y-%m-%d %H:%M:%S", localtime()), "transferin", other_acc.owner.name)
        self.bankTransaction.append(transaction)
    
    @abstractmethod
    def accountDetail(self):
        raise NotImplementedError("You should probably define accountDetail")
    
    def getBalance(self):
        return self.balance
    
    # @abstractmethod
    # def printStatus(self):
    #     raise NotImplementedError("You should probably define printStatus")
    
    def printStatus(self):
        print(f"\t{self.accountDetail()}")

    def printTransaction(self):
        for transaction in self.bankTransaction:
            transaction.printDetail()
            print()
    
class SavingAccount(Account):
    def __init__(self, balance=0, owner=None, interest=1.0):
        super().__init__(balance, owner)
        self.interest = interest

    def __str__(self):
        return f"{self.owner}'s Saving Account"

    def withdraw(self, m):
        if self.balance - m < 0: # if balance after withdrawal is less than 0, don't allow withdrawal
            return False
        old_balance = self.balance
        self.balance -= m
        transaction = BankTransaction(m, self.balance, old_balance, strftime("%Y-%m-%d %H:%M:%S", localtime()), "withdrawal")
        self.bankTransaction.append(transaction)
        return True
    
    def transfer(self, m, other_acc):
        if self.balance - m < 0: # if balance after transfer is less than 0, don't allow transfer
            return False
        old_balance = self.balance
        self.balance -= m
        transaction = BankTransaction(m, self.balance, old_balance, strftime("%Y-%m-%d %H:%M:%S", localtime()), "transfer", other_acc.owner.name)
        self.bankTransaction.append(transaction)
        other_acc.transferIn(m, self)
        return True
    
    def accountDetail(self):
        return f"Saving Account of Customer: {self.owner.name}, Balance: {self.balance}, Interest: {self.interest}"
    
    # def printStatus(self):
    #     print(f"Customer Name: {self.owner}")
    #     print(f"\t{self.accountDetail()}")
    
class CurrentAccount(Account):
    def __init__(self, balance=0, owner=None, limit=-5000):
        super().__init__(balance, owner)
        self.limit = limit

    def __str__(self):
        return f"{self.owner}'s Current Account"

    def withdraw(self, m):
        if self.balance - m < self.limit: # if balance after withdrawal is less that the limit set, don't allow withdrawal
            return False
        old_balance = self.balance
        self.balance -= m
        transaction = BankTransaction(m, self.balance, old_balance, strftime("%Y-%m-%d %H:%M:%S", localtime()), "withdrawal")
        self.bankTransaction.append(transaction)
        return True
    
    def transfer(self, m, other_acc):
        if self.balance - m < self.limit: # if balance after transfer is less than limit, don't allow transfer
            return False
        old_balance = self.balance
        self.balance -= m
        transaction = BankTransaction(m, self.balance, old_balance, strftime("%Y-%m-%d %H:%M:%S", localtime()), "transfer", other_acc.owner.name)
        self.bankTransaction.append(transaction)
        other_acc.transferIn(m, self)
        return True

    def accountDetail(self):
        return f"Current Account of Customer: {self.owner.name}, Balance: {self.balance}, Limit: {self.limit}"
    
    # def printStatus(self):
    #     print(f"Customer Name: {self.owner}")
    #     print(f"\t{self.accountDetail()}")