class Ticket:
    def __init__(self,number):
        self.__number = number

    def getNumber(self):
        return self.__number

    def getPrice(self):
        return self.__price

    def toString(self,ticketNumber,ticketPrice):
        print("Number : ",self.ticketNumber,", Price : ", self.ticketPrice)

class WalkUpTicket(Ticket):
    def __init__(self,number):
        super().__init__(number)
        self.__day = day
    def getPrice(self):
        return 50

class AdvanceTicket(Ticket):
    def __init__(self,number,day):
        self.__number=super().__init__(number)
        self.__day=day

    def getPrice(self):
        if(self.__day>=10):
            return 30
        else:
            return 40

class StudentAdvanceTicket(AdvanceTicket):
    def __init__(self,number,day):
        super().__init__(number,day)

    def getPrice(self):
        return (super(StudentAdvanceTicket,self).getPrice())/2

    def toString(self):
        number = super().getNumber()
        price=super(StudentAdvanceTicket,self).getPrice()/2
        print("Number : ",number,", Price : ",price)

student=StudentAdvanceTicket(1,5)
student.getPrice()
student.toString()
