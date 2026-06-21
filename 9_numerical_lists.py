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

# ==========================
# HOMEWORK
# ==========================

# 1. Use range() to print numbers from 1 to 30 using a for loop.
#    Try printing each number on a new line.

# 2. Create a list using range() that contains numbers from 1 to 500.
#    Print only the first 10 and last 10 values to check it.

# 3. Use range() to generate numbers from 1 to 100.
#    Then use:
#    - min()
#    - max()
#    - sum()
#    Print all results clearly.

# 4. Use range() to generate all even numbers from 1 to 50.
#    Store them in a list and print the list.

# 5. Use range() to generate all odd numbers from 1 to 50.
#    Print each number using a for loop.

# 6. Create a list of the first 10 square numbers using:
#    - a for loop OR list comprehension
#    Example: 1^2, 2^2, 3^2, ...

# 7. Create a list of the first 10 cube numbers using list comprehension.
#    Then print each value using a for loop.

# 8. Challenge:
#    Create a list of numbers from 1 to 100.
#    Then create a second list that contains only numbers
#    that are divisible by 3.
#    Print both lists.