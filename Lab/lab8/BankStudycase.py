import ZODB, ZODB.config
import persistent
from abc import ABC, abstractmethod

class Customer(persistent.Persistent):
    def __init__(self, name = " "):
        self.name = name
        self.accounts = persistent.list.PersistentList()

    def __str__(self):
        return "Customer Name: " + self.name

    def setName(self, n):
        self.name = n

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
            print("", end="     ")
            a.printStatus()

class Account(ABC):
    def __init__(self, balance = 0.0, owner = None):
        self.balance = balance
        self.owner = owner

    @abstractmethod
    def __str__(self):
        raise NotImplementedError('users must define __str__ to use this base class')
    
    def deposit(self, m):
        self.balance += m
    
    def withdraw(self, m):
        self.balance -= m

    def tranfer(self, m, o):
        self.withdraw(m)
        o.deposit(m)
    
    def tranferIn(self, m, o):
        self.deposit(m)
        o.withdraw(m)
    
    def accounDetail(self):
        return self.__str__()
    
    def getBalance(self):
        return self.balance
    
    def printStatus(self):
        print(self.__str__(), "Balance: ", self.balance)

##################################################################################

class CurrentAccount(Account, persistent.Persistent):
    def __init__(self, balance = 0.0, owner = None, limit = -5000.0):
        Account.__init__(self, balance, owner)
        self.limit = limit
    
    def accounDetail(self):
        return super().accounDetail() + " Limit: " + str(self.limit)
    
    def deposit(self, m):
        self.balance += m

    def withdraw(self, m):
        if self.balance - m >= self.limit:
            self.balance -= m
        else:
            print("Insufficient funds")

    def getBalance(self):
        return self.balance
    
    def printStatus(self):
        return super().printStatus()
    
    def tranfer(self, m, o):
        if self.balance - m >= self.limit:
            self.withdraw(m)
            o.deposit(m)
        else:
            print("Insufficient funds")

    def tranferIn(self, m, o):
        self.deposit(m)
        o.withdraw(m)

##################################################################################

class SavingAccount(Account, persistent.Persistent):
    def __init__(self, balance = 0.0, owner = None, interest = 1.0):
        Account.__init__(self, balance, owner)
        self.interest = interest
    
    def accountDeatil(self):
        return super().accounDetail() + " Interest: " + str(self.interest)
    
    def deposit(self, m):
        self.balance += m

    def withdraw(self, m):
        if self.balance - m >= 0:
            self.balance -= m
        else:
            print("Insufficient funds")

    def getBalance(self):
        return super().getBalance()
    
    def printStatus(self):
        return super().printStatus()
    
    def tranfer(self, m, o):
        if self.balance - m >= 0:
            self.withdraw(m)
            o.deposit(m)
        else:
            print("Insufficient funds")

    def tranferIn(self, m, o):
        self.deposit(m)
        o.withdraw(m)

##################################################################################
