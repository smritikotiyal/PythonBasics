class Ticket:
    def __init__(self,Number):
        self.Number=Number

    def getPrice(self):
        pass

    def toString(self,cost):
        print("Number : ",self.Number,", Price: ",cost)

class WallUp(Ticket):
    def __init__(self,Number,days):
        super().__init__(Number)
        self.days=days

    def getPrice(self):
        if(self.days==0):
            return 50

class Advance(Ticket):
    def __init__(self,Number,days):
        super().__init__(Number)
        self.days=days

    def getPrice(self):
        if(self.days>=10):
            return 30
        else:
            return 40

class StudentAdvance(Advance):
    def __init__(self,Number,days):
        super().__init__(Number,days)

    def getPrice(self):
        if(self.days>=10):
            return super(StudentAdvance,self).getPrice()/2
        else:
            return super(StudentAdvance,self).getPrice()/2

ticket1=WallUp(1,0)
cost1=ticket1.getPrice()
ticket1.toString(cost1)

ticket2=Advance(2,20)
cost2=ticket2.getPrice()
ticket2.toString(cost2)

ticket3=StudentAdvance(3,20)
cost3=ticket3.getPrice()
ticket3.toString(cost3)


