def add(x, y):
    print(x + y)
def subtract(x, y):
    print(x - y)
def multiply(x, y):
    print(x * y)
def divide(x, y):
    print(x / y)
n1 = input("Enter first number: ")
n2 = input("Enter second number: ")
op = input("Enter the operation +, -, *, / : ")
if op == '+':
    add(int(n1), int(n2))
elif op == '-':
    subtract(int(n1), int(n2))
elif op == '*':
    multiply(int(n1), int(n2))
elif op == '/':
    divide(int(n1), int(n2))
else:
    print("Invalid entry")
 
O/P:
Enter first number: 12
Enter second number: 15
Enter the operation +, -, *, / : /
0.8
