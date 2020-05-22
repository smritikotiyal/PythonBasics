#Q3
"""a=[2,6,7,45,23,53,14,45,89,5]
a.reverse()
for i in a:
    print(i)

print(a)"""

#Q5
"""cap=int(input("Enter the length of the list:"))
s=[]
for i in range(0,cap):
    n=int(input("Enter the element in the list :"))
    s.append(n)

index_1=int(input("Enter the first index:"))
index_2=int(input("Enter the second index:"))

temp=s[index_1]
s[index_1]=s[index_2]
s[index_2]=temp

print(s)"""

#Q6
"""a=[4,67,45,3,67,3,2]
b=[34,56,2,68,3]
a.extend(b)
print(a)"""

#Q7
"""cap=int(input("Enter the length of the list:"))
s=[]
for i in range(0,cap):
    n=int(input("Enter the element in the list :"))
    s.append(n)

number=int(input("Enter the number to be searched:"))
s.reverse()
i=0
while(i<cap):
    if(s[i]==number):
        index=len(s)-(i+1)
        print(index)
        break
    i+=1
else:
    print(-1)"""

"""l1=[74, 85, 102, 99, 101, 85, 56]
number=int(input("Enter the number to be searched:"))
flag=0

for i in range(len(l1)-1,0,-1):
    if(l1[i]==number):
        print(i)
        flag=1
        break
if(flag==0):
    print(-1)"""



#Q8
"""cap=int(input("Enter the length of the list:"))
s=[]
for i in range(0,cap):
    n=int(input("Enter the element in the list :"))
    s.append(n)
max_num=max(s)
min_num=min(s)

range_num=(max_num-min_num)+1
print(range_num)"""

#13

"""l1=[1,2,3,4,5,6,7]
start=0
end=len(l1)-1
mid=len(l1)//2
l2=[]

if(len(l1)%2==0):
    while(mid<=end):
        l2.append(l1[start]+l1[end])
        start+=1
        end-=1
else:
    while(start!=end):
        l2.append(l1[start]+l1[end])
        start+=1
        end-=1
    l2.append(l1[mid])

print(l2)"""

#9
"""cap=int(input("Enter the length of the list:"))
l1=[]
for i in range(0,cap):
    n=int(input("Enter the element in the list :"))
    l1.append(n)

min_val=int(input("Enter the minimum value:"))
max_val=int(input("Enter the maximum value:"))

count=0
l2=[]
for number in l1:
    if(min_val<=number<=max_val):
        count+=1
        l2.append(number)

print(count)
print(l2)"""

#10
"""cap=int(input("Enter the length of the list:"))
l1=[]
for i in range(0,cap):
    n=float(input("Enter the element in the list :"))
    l1.append(n)
flag=0
for i in range(0,len(l1)-1):
    if(l1[i] > l1[i+1]):
        print('False')
        print(l1[i])
        print(l1[i+1])
        flag=1
        break

if(flag==0):
    print('True')"""
    





















    

    


