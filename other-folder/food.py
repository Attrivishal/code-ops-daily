import sys

print("== SMART FOOD PROGRAM! ==")
# only when name is provided as command line argument
if len(sys.argv) > 1:
    name = sys.argv[1]
    print(f"hello,{name}! Welcome to the Smart Food Program.")

# only when both food and name arguments
if len(sys.argv) > 2:
    food = sys.argv[2]
    print(f"{name} loves {food}")

# only we have three arguments
if len(sys.argv) > 3:
    age = sys.argv[3]
    print(f"{name} is {age} years old and loves {food}.")


# else:
#     print("Please provide your name, favorite food, and age!")
#     print("Example: python food.py Alice Pizza 30")
