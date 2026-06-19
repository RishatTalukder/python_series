# range() is a built-in function that generates a sequence of numbers. 
nums = range(10)

#range takes three parameters: start, stop, and step. 
# start is the number that the sequence starts with. If not specified, it defaults to 0.
# stop is the number that the sequence stops at. This number is not included in the sequence
# step is the difference between each number in the sequence. If not specified, it defaults to 1.
print(list(range(10, 21, 1)))
# you can directly convert the range object to a list using the list() function like above.

# print the squares of the first 100 numbers using a for loop and range.    
for i in range(1, 101, 1):
    print(i**2)
    
# print the odd numbers between 1 and 100 using a for loop and range.
for i in range(1, 101, 2):
    print(i)
    
# create a list of the even numbers between 1 and 100 using a for loop and range.    
empty_list = []

for i in range(0,101,2):
    empty_list.append(i)
    
print(empty_list)

# use the min(), max(), and sum() functions to find the minimum, maximum, and sum of the list.
print(max(empty_list))
print(min(empty_list))
print(sum(empty_list))

# use a list comprehension to create a list of the squares of the odd numbers between 1 and 100.
nums = [i**2 for i in range(1, 101, 2)]
print(nums)

# HOMEWORK

# 1. Use a for loop to print the numbers from 1 to 20, inclusive.

# 2. Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window.)

# 3. Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.

# 4. Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.

# 5. Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

# 6. A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.

# 7. Use a list comprehension to generate a list of the first 10 cubes.