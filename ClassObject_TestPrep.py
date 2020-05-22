import math
class Point:
    total = 0
    def __init__(self,X,Y):
        self.x=X
        self.y=Y
        Point.total +=1

    def translate(self,dX,dY):
        self.x=self.x+dX
        self.y=self.y+dY

    def distance(self, p):
        dx=self.x-p.x
        dy=self.y-p.y
        dist = math.sqrt(pow(dx,2)+pow(dy,2))
        return dist

    def distanceFromOrigin(self):
        dx=self.x-0
        dy=self.y-0
        dist = math.sqrt(pow(dx,2)+pow(dy,2))
        return dist

    def isVertical(self,p):
        if(self.x==p.x):
            return True
        else:
            return False

    def slope(self,p):
        dx=p.x-self.x
        dy=p.y-self.y
        return dy/dx

    @staticmethod
    def totalPoints():
        print('Total points created : ', Point.total)


class Line:
    def __int__(self,newp1=Point(2,3),newp2=Point(4,5)):
        self.p1=newp1
        self.p2=newp2

    def getP1(self):
        return self.p1

    def getP2(self):
        return self.p2

    def getSlope(self):
        dx= (self.p1.x - self.p2.x)
        dy= (self.p2.y-self.p2.y)
        return dy/dx

    def length(self):
        dx = (self.p1.x - self.p2.x)
        dy = (self.p1.y - self.p2.y)
        dist = math.sqrt(pow(dx,2)+pow(dy,2))
        return dist

'''p1=Point(2,3)
p1.translate(1,1)
p2=Point(9,19)
p3=Point(5,3)
dist = p2.distance(p1)
print('Distance between 2 points : ', round(dist,2))
distFromO = p2.distanceFromOrigin()
print('Distance between 2 points : ', round(distFromO,2))
Point.totalPoints()
print(p1.x)
result=p3.isVertical(p1)
print(result)
slope=p3.slope(p1)
print('Slope: ',slope)'''

#p=Line()
#print(p.getP1())
print(Line.getP1())
#slope=p.getSlope()
#print(slope)
