 row = int(input("Enter number of rows (even): "))
n = row//2
print("Generated butterfly pattern is:\n")
for i in range(1,n+1):
    for j in range(1, 2*n+1):
        if j>i and j< 2*n+1-i:
            print("  ", end="")
        else:
            print("* ", end="")
    print()
for i in range(n,0,-1):
    for j in range(2*n,0,-1):
        if j>i and j< 2*n+1-i:
            print("  ", end="")
        else:
            print("* ", end="")
    print()   


O/P:
Enter number of rows (even): 15
Generated butterfly pattern is:


*                         * 
* *                     * * 
* * *                 * * * 
* * * *             * * * * 
* * * * *         * * * * * 
* * * * * *     * * * * * * 
* * * * * * * * * * * * * * 
* * * * * * * * * * * * * * 
* * * * * *     * * * * * * 
* * * * *         * * * * * 
* * * *             * * * * 
* * *                 * * * 
* *                     * * 
*                         * 
