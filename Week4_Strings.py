'''import re
x=re.findall('[a-z]+','Now is the time')
y=re.search('[a-z]+','Now is the time')
print(x)
print(y)'''

'''ab_string = 'abababababababab'
length=len(ab_string)
a_string=ab_string[0]
for i in range(1,length):
    if(i%2==0):
        a_string += ab_string[i]

print(a_string)'''
'''str1='Who’s on first?'

ind1=str1.find('o')
ind2=str1.find('o',ind1+1)

print(ind1,ind2)'''


'''str1='Chapman, Graham Arthur'
length=len(str1)
new_str= ''
for i in range(0,length):
    if(str1[i]==','):
        new_str += str1[i+2:] + ' ' +str1[0:i]
print(str1)
print(new_str)'''

'''print('dog' + 's')
print('dog' - 'g')'''

import re

user_str='11,22,33'

x=re.split(',',user_str)

for i in x:
    print(i)


























