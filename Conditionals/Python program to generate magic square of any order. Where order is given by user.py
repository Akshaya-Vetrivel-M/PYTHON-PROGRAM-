import numpy as np
import sys
order = int(input("Enter order of magic square (order must be odd): "))
if order%2==0:
    order = order+1
    print("Given order is even so it is incremented by 1.")
mid = order//2
magic = np.zeros((order,order))
k = mid
j = 0
for i in range(1,order*order+1):
    magic[j][k] = i
    p = j
    j = j-1
    q = k
    k = k+1
    if j<0:
        j = order-1
    if k>order-1:
        k = 0
    if magic[j][k]!=0:
        k = q
        j = p+1
print("Generated Magic Square is: \n")
for j in range(order):
    print("|", end="")
    for k in range(order):
        print("%4d |" % magic[j][k], end="")
    print()
    for i in range(1, 6*order+1):
        print("-", end="")
    print()

O/P:
Enter order of magic square (order must be odd): 5
Generated Magic Square is: 

|  17 |  24 |   1 |   8 |  15 |
------------------------------
|  23 |   5 |   7 |  14 |  16 |
------------------------------
|   4 |   6 |  13 |  20 |  22 |
------------------------------
|  10 |  12 |  19 |  21 |   3 |
------------------------------
|  11 |  18 |  25 |   2 |   9 |
------------------------------
