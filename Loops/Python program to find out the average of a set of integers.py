count = int(input("Enter the count of numbers: "))
i = 0
sum = 0
for i in range(count):
    x = int(input("Enter an integer: "))
    sum = sum + x
avg = sum/count
print(" The average is: ", avg)

Output:
Enter the count of numbers: 5
Enter an integer: 3
Enter an integer: 2
Enter an integer: 6
Enter an integer: 1
Enter an integer: 4
The average is:  3.2
