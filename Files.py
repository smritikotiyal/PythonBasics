my_file=open("temp.txt","w")
print("My Name is John.", file=my_file)
print("I am studying Software Development. I live in Bradford", file=my_file)
my_file.write("This is the second method of writing to a file.\n")
my_file.write("Data can be written to a file by a print() and method() methods. Syntax differs in both.\n")
lines= ["The next method is by using writelines().\n", "A list of lines needs to be created first and then written to the file by calling writelines() method.\n",
        "I think this is the end of the methods.\n"]
my_file.writelines(lines)
my_file.close()

my_file_read=open("temp.txt","r")
print(my_file_read.read(1))
print(my_file_read.read(5))
print(my_file_read.readline())
print(my_file_read.readline(15))
print(my_file_read.readlines())
for line in my_file_read:
    print(line)
my_file_read.close()
