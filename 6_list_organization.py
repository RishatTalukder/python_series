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

# HOMEWORK

# 1. Seeing the World: Think of at least five places in the world you’d like to visit.
#   •Store the locations in a list. Make sure the list is not in alphabetical order.
#   •Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
#   •Use sorted() to print your list in alphabetical order without modifying the actual list.
#   •Show that your list is still in its original order by printing it.
#   •Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
#   •Show that your list is still in its original order by printing it again.
#   •Use reverse() to change the order of your list. Print the list to show that its order has changed.
#   •Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#   •Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#   •Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.

# 2. Working with one of the programs from the previous exercise in the 5_lists_operations.py file. use len() to print a message indicating the number of people you are inviting to dinner.

# 3. Think of something you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.