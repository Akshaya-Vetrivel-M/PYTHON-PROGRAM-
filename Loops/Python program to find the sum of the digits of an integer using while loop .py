sum = 0
number = int(input("Enter an integer: "))
while(number!=0):
    digit = number%10
    sum = sum+digit
    number = number//10
print("Sum of digits is: ", sum)

Output:
Enter an integer: 25
Sum of digits is:  7
