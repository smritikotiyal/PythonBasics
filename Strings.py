#Q10
"""S="I had a cat named amanda when I was littleaaaa"
count=0
i=0
while(i<len(S)):
    if(S[i]=="a"):
        count+=1
    i+=1
print(count)"""

""">>> s="Topkapi"
>>> s.rjust(20,".")
'.............Topkapi'
>>> s.ljust(15)
'Topkapi        '
>>> s
'Topkapi'
>>> s.find("kap")
3
>>> s.find("kap0")
-1
>>> s="NEW YORK"
>>> s.capitalize
<built-in method capitalize of str object at 0x03A8AB60>
>>> s.capitalize()
'New york'
>>> s.title()
'New York'
>>> """
#Q23
"""name_str='Albert Einstein'
print(name_str.split(' ')[1])

first_name=name_str[:name_str.find(' ')]
last_name=name_str[name_str.find(' ')+1:]
print(first_name,'\n',last_name)"""

#Q24
"""brit_word = 'flavour'
amer_word=brit_word.replace('ur','r')
#amer_word = brit_word.replace('u','')
print(amer_word)"""

#Q26
"""X = 'Alan Turing'
Y=X[::-1]
print(Y)"""

#Q27
"""ab_string = 'abababababababab'
a_string=ab_string.replace('b','')
print(a_string)"""

#Q28
"""a='abcdefghij'
print(a[::-1],'\n',a[::3],'\n',a[8::-2])"""

#Q29
"""str_input="Who’s on first?"
first_index=str_input.find('o')
second_index=str_input.find('o',first_index+1)
print(first_index,\
      second_index)"""

#Q30
"""str_input="Chapman, Graham Arthur"
print(str_input.split(',')[1],str_input.split(',')[0])"""

"""name = 'Chapman , Graham Arthur'
last, comma, first, middle = name.split()

transformed = first + ' ' + middle + ' ' + last

print(transformed)"""






