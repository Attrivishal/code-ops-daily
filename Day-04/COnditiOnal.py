# explain the use of conditional statements in Python
# tell me shortly about it with examples
# Conditional statements in Python are used to perform different actions based on whether a certain condition is true or false. The main conditional statements in Python are `if`, `elif`, and `else`.

# Example 1: Simple if statement using cmmand line argument (sys module)
import sys
from emoji import emojize  # Add this import
# eg.2 
name = sys.argv[1]  # This will fail if you only give 1 argument!
if name == "vishal":
    print(emojize(":waving_hand: Hello Vishal, Welcome back!"))
else:
    print(emojize(":waving_hand: Hello, Try Again!"))

# Example 2: if-elif-else statement
type = sys.argv[2]  # This will fail if you only give 1 argument!
if type == "t2.micro":
    print(emojize(":money_bag: user charged $0.0116 per hour"))
elif type == "t2.small":
    print(emojize(":warning:  YOu are trying tO create  `${t2.small}`, it will charged $0.023 per hour"))
elif type == "t2.medium":
    print(emojize(":check_mark_button: Yes i can create instance for you, but it will cost you $0.0464 per hour"))
else:
    print(emojize(":cross_mark: Instance type not recognized. Please choose a valid type."))