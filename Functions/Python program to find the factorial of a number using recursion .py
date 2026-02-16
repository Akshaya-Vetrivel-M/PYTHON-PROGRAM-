def fact(n):
    if n==1:
        f=1
    else:
        f = n * fact(n-1)
    return f
num = int(input("Enter an integer: "))
result = fact(num)
print("The factorial of", num, " is: ", result)

Output:
Enter an integer: 26
The factorial of 26  is:  403291461126605635584000000
