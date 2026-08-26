# ==========================
# REMOVE ALL OCCURRENCES
# ==========================

pets = [
    "dog",
    "cat",
    "cow",
    "rabbit",
    "cow",
    "cow"
]

while "cow" in pets:
    pets.remove("cow")

print(pets)

# ==========================
# PROCESS ITEMS UNTIL EMPTY
# ==========================

names = [
    "rishat",
    "itvaya",
    "shagor"
]

while names:

    name = names.pop()

    print(f"Welcome to the party, {name.title()}!")

print("All guests have been processed.")

# ==========================
# MOVE ITEMS BETWEEN LISTS
# ==========================

sandwich_orders = [
    "tuna",
    "chicken",
    "beef"
]

finished_sandwiches = []

while sandwich_orders:

    current_order = sandwich_orders.pop()

    print(f"I made your {current_order} sandwich.")

    finished_sandwiches.append(current_order)

print("\nFinished sandwiches:")

for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
    

# ==========================
# REMOVE UNAVAILABLE ITEMS
# ==========================

sandwich_orders = [
    "pastrami",
    "tuna",
    "pastrami",
    "beef",
    "pastrami"
]

print("Sorry, we are out of pastrami.\n")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print(sandwich_orders)

# ==========================
# COLLECT USER INPUT
# ==========================

responses = {}

while True:

    name = input("Enter your name (q to quit): ")

    if name == "q":
        break

    vacation = input("Where would you like to travel? ")

    responses[name] = vacation

print("\nPoll Results:")

for name, place in responses.items():
    print(
        f"{name.title()} wants to visit {place.title()}."
    )
    
# ==========================
# HOMEWORK
# ==========================

# 1. Create a list with repeated values.
#    Use a while loop to remove all occurrences
#    of one specific value.

# 2. Create a list of tasks.
#    Use pop() inside a while loop to process
#    each task until the list becomes empty.

# 3. Create two lists:
#    - pending_tasks
#    - completed_tasks
#    Move tasks from the first list to the second
#    using a while loop.

# 4. Create a list of food orders that contains
#    one unavailable item several times.
#    Remove all unavailable items before processing
#    the remaining orders.

# 5. Create a polling program.
#    Ask users for:
#    - their name
#    - their favorite programming language
#    Store the answers in a dictionary and print
#    all responses at the end.

# 6. Modify the polling program so the user can
#    stop by entering "quit".

# 7. Challenge:
#    Create a simple voting system.
#
#    Ask users for:
#    - their name
#    - their chosen candidate
#
#    Store votes in a dictionary and print the
#    final vote summary after the poll ends.