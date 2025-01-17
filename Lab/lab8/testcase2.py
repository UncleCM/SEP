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
    for customer in root.customers:
        obj = root.customers[customer]
        obj.printStatus()
        print()
        index = 0
        while obj.getAccount(index) != None:
            obj.getAccount(index).printTransaction()
            print()
            index += 1