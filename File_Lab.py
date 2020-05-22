"""my_file=open("temp.txt","r")
lines=my_file.readlines()
my_file_write=open("that.txt","w")
my_file_write.writelines(lines)
my_file.close()
my_file_write.close()

my_file_read=open("that.txt","r")
print(my_file_read.read())
my_file_read.close()"""

my_file=open("test.txt","w")
my_file.write("abcdefghijklmnopqrst")
my_file.close()

test_read= open("test.txt","r")
print(test_read.read())
test_read.close()

newtest_read= open("test.txt","r")
newtest_write=open("newtest.txt","w")

i=1
while(i<=4):
    newtest_write.writelines(newtest_read.readline(5) + "\n")
    i+=1

newtest_write.close()
newtest_read.close()

test_read= open("newtest.txt","r")
print(test_read.read())
test_read.close()