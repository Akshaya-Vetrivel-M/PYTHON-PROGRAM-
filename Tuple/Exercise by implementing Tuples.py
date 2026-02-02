nums = (10, 20, 30, 40, 50, 20)
print("Original Tuple:", nums)

print("First:", nums[0])
print("Last:", nums[-1])

print("Slice:", nums[1:5])
print("Count of 20:", nums.count(20))
print("Index of 40:", nums.index(40))
print("Length:", len(nums))
print("Max:", max(nums))
print("Min:", min(nums))
print("Sum:", sum(nums))

new_tuple = nums + (60, 70)
print("Concatenated:", new_tuple)

repeat_tuple = nums * 2
print("Repeated:", repeat_tuple)

Output:
Original Tuple: (10, 20, 30, 40, 50, 20)
First: 10
Last: 20
Slice: (20, 30, 40, 50)
Count of 20: 2
Index of 40: 3
Length: 6
Max: 50
Min: 10
Sum: 170
Concatenated: (10, 20, 30, 40, 50, 20, 60, 70)
Repeated: (10, 20, 30, 40, 50, 20, 10, 20, 30, 40, 50, 20)
