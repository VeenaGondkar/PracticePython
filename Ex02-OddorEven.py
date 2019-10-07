'''Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''

print("This program identifies if the number is odd or even")

num = int(input("Enter a number: "))
if (num % 2 == 0):
    if (num % 4 == 0):
        print("%d is even number and divisible by 4" %num)
    else:
        print("%d is even number" %num)
else:
    print("%d is odd number" %num)



print("Enter two numbers to check if first number is divisible with second number")
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

if (num1 % num2 == 0):
    print("%d is divisible with %d" %(num1, num2))
else:
    print("%d is not divisible with %d" %(num1, num2))




