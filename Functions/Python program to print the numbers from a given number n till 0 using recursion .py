def print_till_zero(n):
    if (n==0):
        return
    print(n)
    n=n-1
    print_till_zero(n)
print_till_zero(8)


Output:
8
7
6
5
4
3
2
1
