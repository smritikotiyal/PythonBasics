"""j=4
for i in range(1,7):
    print(j, end=" ")
    j=j+15"""

"""j=30
for i in range(1,7):
    print(j, end=" ")
    j=j-10"""

"""j=-7
for i in range(1,7):
    print(j, end=" ")
    j=j+4"""

"""j=97
for i in range(1,7):
    print(j, end=" ")
    j=j-3"""
"""j=-4
for i in range(1,7):
    print(j, end=" ")
    j=j+18"""
"""x=1
for i in range(1,8):
    for j in range(1,i+1):
        print(x,end="")
    print()
    x=x+10"""

"""def pay(salPerHour,noOfHours):
    if(noOfHours>0 and noOfHours<=8):
        totalSal=salPerHour*noOfHours
        print("TA's total salary is :",totalSal)
    elif(noOfHours>8):
        extraWorkHours=noOfHours-8
        print("extraWorkHours :",extraWorkHours)
        extraWorkSal=(salPerHour*1.5)
        print("extraWorkSal :",extraWorkSal)
        totalSal=(salPerHour*8)+(extraWorkSal*extraWorkHours)
        print("TA's total salary is :",totalSal)
    else:
        print("Number of working hours is invalid.")

salPerHour=float(input("Enter the TA's salary earened per hour: "))
noOfHours=int(input("Enter the TA's total working hours: "))
pay(salPerHour,noOfHours)"""

"""from math import * 
def area(radiusCircle):
    return pi*pow(radiusCircle,2)

radiusCircle=float(input("Enter the radius of the circle: "))
areaCircle=area(radiusCircle)
print("The area of the circle is :", areaCircle)"""

"""low = int(input("low? "))
high = int(input("high? "))
sum = 0
for i in range(low,high):
    sum += i
print("sum = " , sum)"""


"""num=1
sum=0
while(num!=0):
    num=int(input("Enter a number : "))
    sum=sum+num

print("Sum = ",sum)"""

"""def rep1(repString, repTimes):
    if(repTimes>0):
        return repString*repTimes
    else:
        return " "

resultString=rep1("hello",0)
if(resultString==" "):
    print("An Empty string has been returned.")
else:
    print(resultString)"""


"""def printRange(x,y):
    if(x<y):
        for i in range(x,y+1):
            print(i," ",end=" ")
        print()
    elif(x>y):
        #i=x
        while(x>=y):
            print(x," ",end=" ")
            x=x-1
        print()
    elif(x==y):
        print(x)

printRange(2,7)
printRange(19,11)
printRange(5,5)"""

"""def smallestLargest():
    num=[] #Empty List
    total=int(input("How many number do you want to enter : "))
    for i in range(0,total):
        print("Number ",i+1," : ", end= " ")
        element=int(input())
        num.append(element)
        #print(num[i])
        
    num.sort()
    print("Smalest = ",num[0])
    print("Largest = ",num[total-1])
   

smallestLargest()"""
"""
def printAverage():
    num=[] #Empty List
    total=int(input("How many number do you want to enter : "))
    for i in range(0,total):
        print("Number ",i+1," : ", end= " ")
        element=int(input())
        num.append(element)
        #print(num[i])
        
    num.sort()
    print("Smalest = ",num[0])
    print("Largest = ",num[total-1])
   

smallestLargest()"""

"""def printAverage():
    num=1
    sum=0
    count=0
    while(num>0):
        num=int(input("Type a number: "))
        if(num>0):
            sum=sum+num
            count=count+1
        elif(count==0 and num<0):
            return -2
    return float(sum/count)

average = printAverage()

if(average!=-2):
    print("Average was ",average)"""


#Method to check Perfect number
def checkPerfect(number):

    #Taking divisors as half the number
    end_limit=int((number/2)+1)
    
    sum_of_divisors=0

    #find and sum up the divisors
    for divisor in range(1,end_limit):
        if(number%divisor==0):
            sum_of_divisors = sum_of_divisors + divisor

    #Print the result
    if(sum_of_divisors == number):
        print(number,"is perfect")
    else:
        print(number,"is not perfect")

#Input from the user
number=int(input("Please enter a number to check : "))

#Call the method
checkPerfect(number)
























        

    
