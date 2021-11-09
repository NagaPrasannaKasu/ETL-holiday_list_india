#Variables

#receiving input
# name = input("What is your name?")
# print("Hallo" +name)

#Type conversation
# birth_year = input("what is your birthday?")
# age = 2021-int(birth_year)
# print(age)
# we have int(), float(), bool(), str() for converting a value or string(converting type of variables)
# first = input("First: ")
# second = input("Second: ")
# sum = float(first)+float(second)
# print("Sum is:" +str(sum))

#Strings
# cource = 'Python learning'
# print(cource.upper())
# print(cource.lower())
# print(cource.find('y')) # prints index of the word 1
# print(cource.find('Python')) # prints index of the word Python 0
# print(cource.replace('for', '4'))
# print('Python' in cource) # True
# print(cource)

#Arithmatic operators
# print(10 / 3) #with this division operator output is 3.3333
# print(10 // 3) #3
# print(10 % 3) # with this modulaer operator output is 1
# print(10 ** 3) # with this exponent operator output is #1000
# x = 10
# x = x+3
# #or
# x += 3 #argumented assignmentet operator

#operator precedence
# we can change it using paranthasis
# x = (10+3)*2

#Comparision operators
# we compare values
# x = 3>2
# >= ,==, <= ,!=

#Logical operators
# boolean expressions
# price = 25
# print(price > 10 and price < 30) # output is TRUE
# print(not price > 10) # it inverses the output, means returns True if answer is False

#IF Statements
# we use to make decisions in our programms
# temperature = 35
# if temperature>30:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif temperature>20:
#     print("It's a nice day")
# elif temperature>10:
#     print("It's a bit cold")
# else:           # if non of the above conditions are true then executes else block
#     print("It's cold")
# print("Done")
# to terminate that if block press shift+tab

# another IF statement example
# weight = int(input("Weight is: "))
# unit = input("(K)g or (L)bs: ")
# if unit.upper() == "K":
#     converted = weight / 0.45
#     print("Weight in Lbs: " + str(converted))
# else:
#     converted = weight * 0.45
#     print("Weight in Kgs: " + str(converted))

#While loop
# i = 1
# while i<=5:
#     print(i)
#     i=i+1
#while loop with expression
# while i<=10:
#     print(i*'*')
#     i=i+1

#Lists
#we know numebr in integers,floats,booleans,strings - basics types in Python
#we also have Lists
# names = ["John","Mob","Sam","Mary"]
# print(names)
# print(names[0])
# print(names[-1]) # prints last element from the list
# print(names[-2]) # print last but one element from the list
# names[0] = "Jon" #updating the name
# print(names[0:3]) # prints elemenst in the indexes 0 to 2

#List methods
# numbers = [1,2,3,4,5,6]
# numbers.append(7)
# print(numbers)
# numbers.insert(0,-1) #inserts a value in the index 0
# print(numbers)
# numbers.remove(5)
# print(numbers)
# print(1 in numbers) # output is TRUE
# print(len(numbers))
# numbers.clear() # it removes all values

#FOR loop
# numbers = [1,2,3,4,5]
# for item in numbers:
#     print(item)
# #same with WHILE loop
# i = 0
# while i<len(numbers):
#     print(numbers[i])
#     i=i+1

#range() funktion
# range funktion is used as part of FOR loop
# numbers = range(5,10)
# numbers = range(5,10,2) # jumps two numbers 5,7,9
# print(numbers)
# for number in numbers:
#     print(number)
#also
# for number in range(5,10,2):
#     print(number)

#Tuples - Tuples are kind of lists used to save the sequence of objects, we cannot change them once we created(unchangable)
# we use square brackets to define a list []
# we use paranthesis to define a Tuples ()
# numbers = (1,2,3)



