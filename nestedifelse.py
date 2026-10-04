# Find the greatest number using nested if else statement.
n1 = int(input("Enter N1"))

n2 = int(input("Enter N2"))

n3 = int(input("Enter N3"))

if n1 > n2:

    if n1 > n3:
        print(n1, " is the greatest number")
    else:
        print( n3, " is the greatest number")

else:
    if n2 > n3:
        print(n2, "is the greatest number")
    else:
        print(n3, "is the greatest number ")


# 2 Question : Take positive integer input and tell if it is divisible by 5 or 3 but not divisible by 15 .
 
    number = int(input("Enter Number"))
    
    if number % 15 == 0:
        print(number,"is divisible by 15")
    else:
        if number % 3 == 0 or number % 5 == 0:
            print(number,"is not divisible by 15 but divisible by 3 or 5")
        else:
            print(number,"is neather divisible by 3 or not divisible by 5")
