nums = list(range(20,51))

print(nums)

# general way to getting a specific section of a list
empty_list = []

for i in range(10, 21):
    empty_list.append(nums[i])
    
print(empty_list)

# using slicing
# list_name[start:end:step]
sliced_list = nums[13::2]
print(sliced_list)

# start index is inclusive and set to 0 by default
sliced_list = nums[:5]
print(sliced_list)

# end index is exclusive and set to the length of the list by default
sliced_list = nums[5:]
print(sliced_list)

# step is set to 1 by default
sliced_list = nums[::3]
print(sliced_list)

# you can also loop through a sliced list
for num in nums[9:14:2]:
    print(num)
    

# negative index also works
#last 5 index values
last_5 = nums[-5:]
print(last_5)

# copying a list with slicing
copied_list = nums[:]
print(copied_list)

# copying a list with copy
copied_list = nums.copy()
print(copied_list)

# changing the value of the copied list will not change the value of the original list
copied_list[15] = 999999
print(copied_list)
print(nums)

# ==========================
# HOMEWORK
# ==========================

# 1. Create a list of at least 10 numbers using range().
#    Print the full list first.

# 2. Use slicing to print:
#    - first 3 items
#    - middle 3 items
#    - last 3 items
#    Add clear messages before each output.

# 3. Create a list of at least 15 items (numbers, names, or anything).
#    Try slicing it in different ways:
#    - first half of the list
#    - second half of the list
#    - every second item
#    Print each result separately.

# 4. Use negative indexing with slicing:
#    - print last 5 items
#    - print last 3 items in reverse order

# 5. Copy a list using:
#    - slicing ([:])
#    - copy() method
#    Modify both copies and observe that original list
#    does not change.

# 6. Loop through a sliced portion of a list.
#    Example: iterate over only a section of the list using slicing.

# 7. Challenge:
#    Create a list using range(1, 50).
#    Then extract:
#    - all even-indexed elements using slicing
#    - every 3rd element
#    Print both results clearly.
