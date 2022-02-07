# Use this interpreter, by typing 'python dsl_interpreter.py habits_tracker.dsl' into the console.
# If you want to use some other .dsl file, just change the path :)

import sys

# my functions:
# (could be outsourced in its own module)

functions = {'Spent': lambda a, b: a + b }

variables = {}

# check if exactly two files are given (interpreter + dsl)
if len(sys.argv) != 2:
    sys.exit(1)

# open .dsl and check each line
with open(sys.argv[1]) as file:
    # initialization for actual parking situation
    category = {"groceries": 0,
               "restaurants": 0,
               "rent": 0,
               "beer": 0,
               "shopping": 0,
               "entertainment": 0
               }

    for line in file:
        line = line.strip()

        # check if the line is a comment
        if not line or line[0] == '*':
            continue
        parts = line.split()
        # print(parts)

        # check the instructions for each line and execute them
        if parts[0] == 'Expenses':
            print("Your expenses in:" + str(category[parts[3]]) + " sums " + parts[3] + "this month")

        else:
            a = category[parts[4]]
            b = int(parts[1])
            category[parts[4]] = functions[parts[0]](a, b)

