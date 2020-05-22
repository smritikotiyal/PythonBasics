"""my_dict={'bill':3,'rich':10}
print(my_dict['bill'])
my_dict['bill']=100
print(my_dict['bill'])
new_dict={'john':2,'mike':4}
print(my_dict.keys())
print(my_dict.values())
my_dict.update(new_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(my_dict.pop('bill'))
print(my_dict.keys())
print(my_dict.values())
copy_dict=my_dict.copy()
print(copy_dict.keys())
print(copy_dict.values())
my_dict['rich']=200
print(my_dict.keys())
print(my_dict.values())
print(copy_dict.keys())
print(copy_dict.values())"""


'''import string

def add_word(word,word_count_dict):
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word]=1

def process_line(line,word_count_dict):
    line=line.strip() #Removes extra precedding or following characters
    line_list= line.split()

    for word in line_list:
        word=word.lower()
        word=word.strip()
        word=word.strip(string.punctuation)
        add_word(word,word_count_dict)

    print(line_list)

word_count_dict={}
my_file=open("temp.txt","r")
for line in my_file:
    #print(line)
    process_line(line,word_count_dict)

for word in word_count_dict:
    print(word, ' = ',word_count_dict[word] )

my_file.close()'''
'''import string

def add_word(word,my_set):
    if(len(word)>3):
        my_set.add(word)


def process_line(line, my_set):
    line=line.strip()
    word_list=line.split()

    for word in word_list:
        word = word.lower()
        word = word.strip()
        word = word.strip(string.punctuation)
        add_word(word,my_set)

a_set=set()
b_set=set()
my_file1=open("temp.txt","r")
my_file2=open("that.txt","r")

for line in my_file1.readline():
    process_line(line,a_set)

for line in my_file2.readline():
    process_line(line,b_set)
my_file1.close()
my_file2.close()

print(a_set)'''

















