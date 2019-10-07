# Python program to check if the input number is prime or not

for j in range(1,100):

# take input from the user
# num = int(input("Enter a number: "))
    num = j
# prime numbers are greater than 1
    if num > 1:
    # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                print(str(num) + " is not a prime number")
                #print(i, "times", num // i, "is", num)
                break
        else:
            print(str(num) + " is a prime number")

# if input number is less than
# or equal to 1, it is not prime
    else:
        print(str(num) + " is not a prime number")