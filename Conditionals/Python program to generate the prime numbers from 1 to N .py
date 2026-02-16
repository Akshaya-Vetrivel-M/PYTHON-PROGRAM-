num =int(input("Enter the range: "))
for n in range(1,num):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        print(n)

Output:
Enter the range: 6
1
2
3
5
