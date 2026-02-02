n = int (input("Enter the limit less than 99999:"))
s=99999
for i in range (1,n+1):
    print ("Enter",i,end='')
    a=int(input("The number :"))
    if a < s:
        s=a
print ("Smallest no.is :",s)        

o/p:
Enter the limit less than 99999:4
Enter 1The number :32
Enter 2The number :21
Enter 3The number :13
Enter 4The number :54
Smallest no.is : 13
