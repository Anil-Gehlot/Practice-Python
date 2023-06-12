
# Example 1: 
from abc import *

class DBInterface(ABC):

    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass

class Oracle(DBInterface):
    def connect(self):
        print('Connecting Oracle Database.')

    def disconnect(self):
        print('disConnecting Oracle Database.')


class Sysbase(DBInterface):
    def connect(self):
        print('Connecting Sysbase Database.')

    def disconnect(self):
        print('disConnecting Sysbase Database.')



dbname = input("Enter database name:")

classname = globals()[dbname]
obj = classname()
obj.connect()
obj.disconnect()

"""
OUTPUT:

Enter database name:Oracle
Connecting Oracle Database.
disConnecting Oracle Database.

Enter database name:Sysbase
Connecting Sysbase Database.
disConnecting Sysbase Database.

Enter database name:abc
KeyError: 'abc'

"""








# Example 2: 
from abc import *

class Printer(ABC):

    @abstractmethod
    def printIt(self, text):
        pass
    @abstractmethod
    def disconnect(self):
        pass

class EPSON(Printer):
    def PrintIt(self, text):
        print('Printing from EPSON Printer.')
        print(text) 

    def disconnect(self):
        print('Printing Completed.')


class HP(Printer):
    def printIt(self,text):
        print('Printing from HP Printer.')
        print(text)

    def disconnect(self):
        print('Printing Completed.') 

text = input("Enter text to print : ")

p = input("Enter printer name: ")

className = globals()[p]

className().printIt(text)
className().disconnect()

'''
OUTPUTL:

Enter text to print : hello I am Prabhas.
Enter printer name: HP
Printing from HP Printer.
hello I am Prabhas.
Printing Completed.
'''