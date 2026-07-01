# tuples
nums = (1,2,3,4,5,6)

# tuple has no assignment feature
# So this will through an error
nums[1] = 10

# indexing works the same as a list
print(nums[1])

# you can also loop through a tuple like a list
for i in nums:
    print(i)
    
# you don't have to put a parenthesis when declaring a tuple
nums = 1,2,3
print(nums)

# If you have a tuple with only one value, python will treat it as a normal integer
nums = (1)
print(nums)

# to tell python that you have a tuple with only one value
nums = (1,)
print(nums)