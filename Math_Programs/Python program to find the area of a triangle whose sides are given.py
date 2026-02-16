import math
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(" Area of the triangle is: ", area)

Output:
Enter the length of side a: 10
Enter the length of side b: 10
Enter the length of side c: 5
 Area of the triangle is:  24.206145913796355
