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
    
# ==========================
# HOMEWORK
# ==========================

# 1. Create a list of at least five numbers.
#    Use a for loop to:
#    - print each number
#    - print each number multiplied by 2

# 2. Modify the loop so that for each number you also print:
#    - the square of the number (num * num)
#    - a message like "Processing number X"

# 3. Create a nested loop:
#    - outer loop: a list of at least 3 items
#    - inner loop: another list of at least 3 items
#    Print something inside both loops to clearly show how nesting works.

# 4. Experiment with indentation:
#    - Try adding a print statement outside the loop
#    - Then move it inside the loop
#    - Observe how the output changes

# 5. Create a list of names.
#    Use a for loop to:
#    - greet each person
#    - print a second line for each person
#    Make sure both lines stay inside the loop.

# 6. Add a final message outside the loop:
#    Example: "Loop has finished running."

# 7. Challenge:
#    Create a nested loop where:
#    - outer loop goes through a list of numbers
#    - inner loop goes through the same list
#    Print both values in each iteration to understand how nested loops behave.