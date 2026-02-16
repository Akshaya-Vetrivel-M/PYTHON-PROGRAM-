c = 0
p = 1.0
count = int(input("Enter the number of values: "))
while(c<count):
    x = float(input("Enter a real number: "))
    c = c+1
    p = p * x
gm = pow(p,1.0/count)
print("The geometric mean is: ",gm)

Output:
Enter the number of values: 2
Enter a real number: 12
Enter a real number: 25
The geometric mean is:  17.320508075688775
