"""for i in range(1,6):
    print('*'*14)

for i in range(1,6):
    for j in range(1,15):
        print('*',end="")
    print()"""


"""for i in range(1,8):
    print(str(i)*i)

for i in range(1,8):
    for j in range(1,i+1):
        print(i,end="")
    print()"""

"""user_money=float(input("Please specify how much money do you have: "))
nin_cost = 100.69

purchasable_units=int(user_money/nin_cost)
leftover_money=user_money%nin_cost
print("leftover_money= ",leftover_money)
print("The user can purchase ",purchasable_units," Nintendo Wiis with the specified amount")
print("The user needs ", nin_cost-leftover_money," more Rs to purchase one additional Wii")"""

"""number=int(input("Enter the number you want to calculate a factorial of:"))
for i in range(number-1,0,-1):
    number*=i
print("The factorial of the number is : ",number)"""


"""number=int(input("Enter the number you want to get the factors of:"))
stop=int(number/2)
print("The factors of ",number," are:")
for i in range(2,stop+1):
    if(number%i==0):
        print(i)"""

"""number=int(input("Enter the number you want to get the factors of:"))
stop=int(number/2)
i=2
while(i<=stop):
    if(number%i==0):
        print(i)
    i+=1"""

"""user_string=input("Enter a string you want to perform rotation cypher on: ")

cypher_string=""
for i in user_string:
    #concat_char=ord(i)+1
    cypher_string+=chr(ord(i)+1)

print(cypher_string)"""

"""print("Hello World",\
      "of continuation")"""

import random
random_number= random.randint(0,101)
print(random_number)
user_guess=int(input("Please enter your guess: "))

while(0<=user_guess<=100):
    
    if(user_guess==random_number):
        print("Congratulations! You guessed the number right. ")
        break
    elif(user_guess>random_number):
        print("The number is lesser than your guess. Please guess again!")
    elif(user_guess<random_number):
        print("The number is greater than your guess. Please guess again!")
        
    #Try again
    user_guess=int(input("Please enter your guess: "))

else:
    print("The entered number is invalid. Try again later.")


















