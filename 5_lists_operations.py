bikes = ["Honda", "Yamaha", "Suzuki"]

print(bikes)

# you can change the value of the list by indexing
bikes[0] = 'harley devidson'
print(bikes)

# you can add a value at the end of the list using append
bikes.append('Ducati')
bikes.append('Kawasaki')
bikes.append('Ducati')
print(bikes)

# If you want to insert a value at a specific index, you can use insert
bikes.insert(1, 'Honda')
print(bikes)

# you can remove a value from the list by indexing
del bikes[2]
print(bikes)

# you can remove a from the end of the list using pop
bikes.pop()
print(bikes)

# pop method can also remove a value from the list by indexing
# and it'll return the value that was removed
pop_value = bikes.pop(1)
print(bikes)
print(pop_value)

# Finally if you want to remove something by `value`, you can use remove method
bikes.remove('Ducati')
print(bikes)

# ==========================
# HOMEWORK
# ==========================

# 1. Create a list of at least four of your favorite games,
#    movies, or programming languages.
#    Print the list before making any changes.

# 2. Replace the first item in the list with a new value
#    using indexing, then print the updated list.

# 3. Add two new items to the end of the list using append().
#    Print the list after each addition.

# 4. Insert a new item at the beginning or middle of the list
#    using insert(), then print the result.

# 5. Remove an item using del and print the updated list.

# 6. Use pop() to remove the last item from the list.
#    Store the removed value in a variable and print:
#    - the updated list
#    - the removed value

# 7. Use pop(index) to remove an item from a specific position.
#    Again, store the removed value in a variable and print both
#    the list and the removed item.

# 8. Add a duplicate value to the list and then remove one
#    occurrence of it using remove().
#    Print the final list.

# 9. Challenge:
#    Create a list with at least five items and perform all of
#    the following operations in order:
#    - append()
#    - insert()
#    - del
#    - pop()
#    - remove()
#    Print the list after every operation so you can clearly
#    see how it changes.