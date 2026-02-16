number = int(input("Enter number: "))
total_sum = 0
step = 1
condition = True
while condition:    
    while number:
        total_sum += number%10
        number //= 10
    print("Step-%d Sum: %d" %(step, total_sum))
    number = total_sum
    total_sum = 0
    step += 1
    condition = number > 9

O/P: 
Enter number: 99999999999
Step-1 Sum: 99
Step-2 Sum: 18
Step-3 Sum: 9
