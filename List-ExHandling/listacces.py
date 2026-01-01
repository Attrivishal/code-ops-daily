# Create a list of 5 colors. ask user for position(0-4) and display the color at that position

colors =["red","blue","green","yellow","purple"]
print("Enter the position of the color you want (0-4)")

try:
      position = int(input())
      color = colors[position]
      print(f"The color position {position} is {color}")
except ValueError:
      print("Error: please enter a valid number (0-4)")
except IndexError:
      print("Error: Position must be between 0 and 4")