'''__init__(String, String,float) is a constructor
getAccountNumber():String returns the account number
getAccountName():String returns the account name
getBalance():float returns the balance
deposit(float)accepts an item of type float and adds it to the balance
withdraw(float): Boolean accepts an item of type float and checks if there are sufficient funds to make a withdrawal.
If there are not, then the method terminates and returns a value of false. If there are sufficient funds, however'''

class BankAccount:

    def __init__(self,accountName,accountNumber,balance):
        self.__accountName=accountName
        self.__accountNumber=accountNumber
        self.__balance=balance

    def getAccountNumber(self):
        return self.__accountNumber

    def getAccountName(self):
        return self.__accountName

    def getBalance(self):
        return self.__balance

    def deposit(self,addMoney):
        self.__balance = self.__balance + self.addMoney

    def withdraw(self,withdrawMoney):
        if(self.__balance>withdrawMoney):
            self.__balance = self.__balance-withdrawMoney
            return True
        else:
            return False

A1=BankAccount('Josh','A12345',2000)
A2=BankAccount('Rach','B54321',3000)
A3=BankAccount('Pheebs','C25324',500)


