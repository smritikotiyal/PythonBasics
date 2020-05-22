'''a=[1,2,3]
b=[5,6,7]

a.append(b)
print(a)

import copy
c=copy.deepcopy(a)
print(c)
b[0]=1000
print(a, b, c)'''

'''L = [1,3,5,7,9]

new_L=L[0:1] + L[2:]
print(new_L)'''



'''def toSort(user_string):
    L1=[]
    for i in user_string:
        L1.append(i)
    L1.sort()

    new_user_string=''
    for i in L1:
        new_user_string+=i
    return new_user_string

result = toSort('Attack')
print(result,type(result))'''



'''def fracAdd(tup1,tup2):
    return ((tup1[0]/tup1[1]) + (tup2[0]/tup2[1]))

def fracMul(tup1,tup2):
    return ((tup1[0]/tup1[1]) * (tup2[0]/tup2[1]))

print(fracAdd((1,2),(2,4)))
print(fracMul((1,2),(2,4)))'''

'''def indexFinder(L1,num):
    print('in func')
    length=len(l1)
    for i in range(length-1,-1,-1):
        if(l1[i]==num):
            print(i)
            break

l1=[74, 85, 102, 99, 101, 85, 56]

indexFinder(l1,85)'''





















