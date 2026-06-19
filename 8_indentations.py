nums = [1,2,3,4,5,6,7,8]

# Indentation is very important in python. 
# Thnk of it like a invisible bracket. It tells python which lines of code belong to a loop, function, if statement, etc.
# Add a tab before a line of code to indent it.
for num in nums:
    print(num)
    print(num*2)
# if you want to add more lines of code to the loop, you have to maintain the same level of indentation of the first line of code in the loop or else you'll get an error.
    

# If you have a code block inside another code block, you have to add another level of indentation for the inner code block. to indicate that it belongs to the inner code block. 
for num in nums:
    print(num)
    
    # inner block should have extra indentation
    for i in nums:
        print(i)
        print("inside loop")
    
    print(num*2)
    
# HOMEWORK

# 1: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
# • Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza.
# • Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

# 2: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
# • Modify your program to print a statement about each animal, such as A dog would make a great pet.
# • Add a line at the end of your program stating what these animals have in common. You could print a sentence such as Any of these animals would make a great pet!