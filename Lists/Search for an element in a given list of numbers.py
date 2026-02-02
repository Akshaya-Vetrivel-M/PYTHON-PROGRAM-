l = [2,58,94,11,32]
n = int (input("Enter the no to be searched :"))
found=0
for x in l:
    if x==n:
        print ("Item found at position:",l.index (n)+1)
        found =1
if found == 0:
    print("Item not found!")

o/p:
Enter the no to be searched :11
Item found at position: 4
