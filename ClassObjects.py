import math
class Point:
    total = 0
    def setLocation(self,X,Y):
        self.x=X
        self.y=Y

    def translate(self,dx,dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def distance(self,p):
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)

    def isVertical(self,p):
        if(self.x == p.x):
            return True
        else:
            return False

    def slope(self,p):
        dx = p.x - self.x
        dy = p.y - self.y
        return dy/dx


class Line:
    def __int__(self,newp1=Point(),newp2=Point()):
        self.p1=newp1
        self.p2=newp2
    def getP1(self):
        return self.p1, self.p2

    def getP2(self):
        return self.x, self.y

#def getSlope(self):
#Return the slope of this Line. The slope of a line between point (x1,y1) and (x2,y2) is equal to (y2-y1)/(x2-x1).
#def getLength(self):
#Return the length of this Line.
#Develop a client program to test your Line class.


    
    #def main():
     #   p1=Point()
      #  p1.setLocation(1,2)
       # p1.translate(2,3)

        #p2=Point()
        #p2.setLocation(1,2)

        #result=p2.distance(p1)
        #print("The distance between the two points is: ",result)
        
