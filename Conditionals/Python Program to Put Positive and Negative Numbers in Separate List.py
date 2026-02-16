NumList = []
Positive = []
Negative = []
Number = int(input("Please enter the Total Number of List Elements : "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)


for j in range(Number):
    if(NumList[j] >= 0):
        Positive.append(NumList[j])
    else:
        Negative.append(NumList[j])
print("Element in Positive List is : ", Positive)
print("Element in Negative List is : ", Negative)

O/P:
Please enter the Total Number of List Elements : 5
Please enter the Value of 1 Element : 2
Please enter the Value of 2 Element : 5
Please enter the Value of 3 Element : 6
Please enter the Value of 4 Element : 2
Please enter the Value of 5 Element : 1
Element in Positive List is :  [2, 5, 6, 2, 1]
Element in Negative List is :  []
