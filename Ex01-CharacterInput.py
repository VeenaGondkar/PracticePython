''' Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

    Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
    Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
'''

import datetime

name = input("Hello. Please tell me your name: ")
age = input("Enter Age: ")
currentyear = datetime.datetime.now().year
bornyear = currentyear - int(age)
years_100_later = bornyear + 100


print(name + " on the %dth year you are going to be 100 years." %(years_100_later) + "\n")
repeat = input("Enter a number you would like this message to be printed : ")
for i in range(0,int(repeat)):
    print(name + " on the %dth year you are going to be 100 years." % (years_100_later) + "\n")