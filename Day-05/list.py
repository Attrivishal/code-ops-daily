# Explain this tOPic in detail with examples: Lists in Python
# Lists in Python are one of the most versatile and commonly used data structures.
#  A list is an ordered collection of items that can hold a variety of data types, including integers, strings, floats, and even other lists. 
# Lists are mutable, meaning that their contents can be changed after they are created.

# Creating a List
# You can create a list by placing comma-separated values inside square brackets [].

students_name =["Radha rani", "Thakur Ji", "Priya Ju","Lal Ju"]
students_name.append("Gopal Ji")  # Adding an item to the list
students_name.append("Vishal")  # Adding an item to the list
students_name.remove("Vishal")  # Removing an item from the list
print(students_name[1])
print( "the length is:-",len(students_name))
print("Students Names:", students_name)

# why this  helpful in devops? 
# In DevOps, lists can be used to manage collections of servers, configurations, or deployment tasks.

# For example, you might have a list of server IP addresses that you need to iterate over to deploy an application.

# Tuples vs Lists
# Tuples are similar to lists, but they are immutable, meaning that once a tuple is created, its contents cannot be changed.
# Lists, on the other hand, can be modified.


name =("Radha rani", "Thakur Ji", "Priya Ju","Lal Ju")  # This is a tuple
print("Names Tuple:", name)
print( "the length in tuple  is:-",len(name)) 

print( "After coNCATE:- ","radha rani" + "-" , "Thakur Ji")  # Concatenating strings