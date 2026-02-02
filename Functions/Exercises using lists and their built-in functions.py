num = [10,20,30,40,50]
print ("Original list : ", num)

num.append(60)
print("After append(60):",num)

num.insert(1,15)
print ("After insert(1,15):", num)

num.remove(30)
print ("After remove(30):", num)

num.pop(2)
print("After pop(2):", num)

num.extend([70,80])
print("After extend([70,80]):", num)

print("Count of 20:", num.count(20))

print("Index of 50:", num.index(50))

num.sort()
print("After sort():", num)

num.reverse()
print("After reverse():", num)

copy_list = num.copy()
print("Copied List:", copy_list)

print("Length of list:", len(num))
print("Maximum value:", max(num))
print("Minimum value:", min(num))
print("Sum of list:", sum(num))
num.clear()
print("After clear():", num)


o/p
Original list :  [10, 20, 30, 40, 50]
After append(60): [10, 20, 30, 40, 50, 60]
After insert(1,15): [10, 15, 20, 30, 40, 50, 60]
After remove(30): [10, 15, 20, 40, 50, 60]
After pop(2): [10, 15, 40, 50, 60]
After extend([70,80]): [10, 15, 40, 50, 60, 70, 80]
Count of 20: 0
Index of 50: 3
After sort(): [10, 15, 40, 50, 60, 70, 80]
After reverse(): [80, 70, 60, 50, 40, 15, 10]
Copied List: [80, 70, 60, 50, 40, 15, 10]
Length of list: 7
Maximum value: 80
Minimum value: 10
Sum of list: 325
After clear(): []
