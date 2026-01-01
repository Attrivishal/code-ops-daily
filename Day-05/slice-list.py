# Slicing the list in pythOn
# Slicing is a powerful feature in Python that allows you to extract a portion of a list (or other sequence types like strings and tuples) by specifying a start and end index.

# The syntax for slicing is: list[start:end], where 'start' is the index to begin the slice (inclusive) and 'end' is the index to end the slice (exclusive).

# Creating a list of numbers
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Slicing from index 2 to 5
slice1 = numbers[2:6]  # This will include elements at index 2, 3, 4, and 5
print("Slice from index 2 to 5:", slice1)  # Output: [30, 40, 50, 60]



# SOrting the list in python

numbers_unsorted = [50, 20, 80, 10, 60, 30, 70, 40, 90, 100]
print(numbers_unsorted.sort())  
print("Sorted List:", numbers_unsorted)  