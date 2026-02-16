numbers = []
num = int(input('How many numbers: '))
for n in range(num):
    x = int(input('Enter number '))
    numbers.append(x)
print("Sum of numbers in the given list is :", sum(numbers))

Output:
How many numbers: 5
Enter number 2
Enter number 12
Enter number 8
Enter number 10
Enter number 6
Sum of numbers in the given list is : 38
