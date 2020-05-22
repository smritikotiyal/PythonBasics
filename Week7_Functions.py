'''def my_func(param_list):
    print(param_list)
    param_list[0]=100
    print(param_list)
    param_list=[1,2,3]
    print(param_list)
    return param_list[0],param_list[1]

arg_list=[1,2,3]
x,y=my_func(arg_list)
print(x)
print(y)'''

'''def my_fun(a,*b):
    print(a)
    print(b)

my_fun(1,2,3,4)'''

'''def checkSort(myList):
    myNewList = sorted(myList)
    print(myNewList)
    print(myList)
    if(myList==myNewList):
        return True
    else:
        return False
result=checkSort([1,2,3,4,5])
print(result)'''

'''def removeEven(myList):
    length= len(myList)
    myNewList=[]
    for i in range(0,length):
        if(myList[i]%2!=0):
            myNewList.append(myList[i])
    return myNewList

def removeOdd(myList):
    length= len(myList)
    myNewList=[]
    for i in range(0,length):
        if(myList[i]%2==0):
            myNewList.append(myList[i])
    return myNewList

def callFun(myList,decision):
    if(decision == True):
        resultEven = removeOdd(myList)
        return resultEven
    else:
        resultOdd = removeEven(myList)
        return resultOdd

resultEven = callFun([1,2,3,4,5],True)
resultOdd = callFun([1,2,3,4,5],False)
print(resultEven)
print(resultOdd)'''




