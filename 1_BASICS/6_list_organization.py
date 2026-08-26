nums = [3,2,5,19,7,4]

#permanently sorted
nums.sort()
print(nums)

nums = [3,2,5,19,7,4]

# sorted but not permanently
sorted_nums = sorted(nums)
print(nums)
print(sorted_nums)

#reverse sorted
reversed_nums = sorted(nums, reverse=True)
print(reversed_nums)
nums.sort(reverse=True)
print(nums)

# sorting will also work with strings
bikes = ["Honda", "Yamaha", "Suzuki"]
bikes.sort(reverse=True)
print(bikes)

# reversing the list
bikes = ["Honda", "Yamaha", "Suzuki"]
bikes.reverse()
print(bikes)

# length of list
item_count = len(nums)
print(item_count)

# out of bounds error
print(bikes[-4])

# ==========================
# HOMEWORK
# ==========================

# 1. Create a list of at least six numbers in random order.
#    - Print the original list.
#    - Use sorted() and print the result.
#    - Print the original list again to verify that it was not changed.

# 2. Take the same list and:
#    - Use sorted(reverse=True)
#    - Print the result in descending order.
#    - Print the original list again.

# 3. Permanently sort the list using sort().
#    Print the list after sorting.

# 4. Permanently sort the list in descending order
#    using sort(reverse=True) and print the result.

# 5. Create a list of at least five strings
#    (for example: countries, games, or programming languages).
#    Sort the list alphabetically and then in reverse order.

# 6. Create another list and use reverse() to reverse
#    the current order of the items.
#    Print the list before and after reversing.

# 7. Use len() to find the total number of items in a list.
#    Print a message like:
#    "This list contains 6 items."

# 8. Challenge:
#    Create a list of your favorite movies, books, or cities.
#    Use every function and method introduced in this lesson:
#    - sorted()
#    - sort()
#    - sort(reverse=True)
#    - reverse()
#    - len()
#    Print the list after every operation and observe
#    which ones modify the original list and which ones don't.