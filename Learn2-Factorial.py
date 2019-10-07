print("Program to find Factorial of a number")

#num = int(raw_input("Enter a integer : "))


for j in range(1,100):
    num = j
    fact = 1
    for i in range(1,num + 1):
        fact = i * fact

    print("Factorial of number : " + str(num) + " is " + str(fact))

