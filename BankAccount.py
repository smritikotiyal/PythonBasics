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
        self.addMoney=addMoney
        self.__balance = self.__balance + self.addMoney
        return self.__balance

    def withdraw(self,withdrawMoney):
        self.withdrawMoney = withdrawMoney
        if(self.__balance>withdrawMoney):
            self.__balance = self.__balance-withdrawMoney
            return True
        else:
            return False

class  VIPBankAccount(BankAccount):
    def __init__(self, accountName, accountNumber, balance, creditlimit):
        super().__init__(accountName,accountNumber,balance)
        self.__creditlimit=creditlimit

    def withdraw(self,withdrawMoney):
        #base_balance=super(VIPBankAccount,self).getBalance()
        balance = super(VIPBankAccount, self).getBalance()
        if(balance>withdrawMoney):
            balance = balance-withdrawMoney
            return True
        elif(self.__creditlimit>withdrawMoney):
            self.__creditlimit=self.__creditlimit-withdrawMoney
            return True
        else:
            return False

def printInfo(acc):
    print("Account Name : ", acc.getAccountName())
    print("Account Number : ", acc.getAccountNumber())
    print("Balance : ", acc.getBalance())
    print("Balance after deposit : ",acc.deposit(100))
    print("Withdrawal Status : ", acc.withdraw(3400))


normal=BankAccount("Normal","A1234",2000.0)
vipAccount=VIPBankAccount("vipAccount","A5678",3000.0,500.0)
printInfo(normal)
printInfo(vipAccount)
