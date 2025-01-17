import ZODB, ZODB.config
import persistent
from abc import ABC, abstractmethod
import BTrees._OOBTree
import transaction
import zodBank

path = "./config.xml"

db = ZODB.config.databaseFromURL(path)
connection = db.open()
root = connection.root

if __name__ == "__main__":
    root.customers = BTrees.OOBTree.BTree()
    root.customers['Dave'] = zodBank.Customer('Dave')
    d = root.customers['Dave']
    root.customers['Jone'] = zodBank.Customer('Jone')
    j = root.customers['Jone']

    print("Create Account:")
    b1 = d.addAccount(zodBank.SavingAccount(400, d))
    b2 = j.addAccount(zodBank.CurrentAccount(200, j))
    d.printStatus()
    j.printStatus()

    print("\nDeposit 500 to Account 2")
    b2.deposit(500)
    b2.printStatus()

    print("\nWithdraw 200 from Account 1")
    b1.withdraw(200)
    b1.printStatus()

    print("\nTransfer 150 from Account 2 to Account 1")
    b2.transfer(150, b1)
    b1.printStatus()
    b2.printStatus()

    transaction.commit()