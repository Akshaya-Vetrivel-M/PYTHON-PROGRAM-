def binarySearch(alist, key) :
    first = 0
    last = len(alist)-1
    found = 0
    while first<=last and not found:
        midpoint = (first+last)//2
        if key==alist[midpoint] :
            found=1
            break
        elif key<alist[midpoint] :
            last=midpoint-1
        else:
            first=midpoint+1
        if found==1:
            print(key , "is found in the list " ,alist ,"at position ",midpoint+1)
        else :
            print(key , "is not found in the list ")
testlist = [2, 4, 6, 8, 10, 12, 14, 16, 5]
binarySearch(testlist, 10)
testlist = [2, 4, 6, 8, 10, 12, 14, 16, 5]
binarySearch(testlist, 2)

O/P:
2 is not found in the list 
2 is not found in the list 
