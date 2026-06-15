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


# HOMEWORK

# 1. If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.

# 2. You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
#   •Start with your program from Exercise 1. Add a print() call at the end
#   of your program stating the name of the guest who can’t make it.
#   •Modify your list, replacing the name of the guest who can’t make it with
#   the name of the new person you are inviting.
#   •Print a second set of invitation messages, one for each person who is still
#   in your list.

# 3. You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
#   •Start with your program from Exercise 1 or Exercise 2. Add a print() call to the end of your program informing people that you found a biggerdinner table.
#   •Use insert() to add one new guest to the beginning of your list.
#   •Use insert() to add one new guest to the middle of your list.
#   •Use append() to add one new guest to the end of your list.
#   •Print a new set of invitation messages, one for each person in your list.

# 4. You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
#   •Start with your program from Exercise 3. Add a new line that prints a message saying that you can invite only two people for dinner.
#   •Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#   •Print a message to each of the two people still on your list, letting them
# know they’re still invited.
#   •Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.