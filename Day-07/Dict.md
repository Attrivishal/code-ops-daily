📘 Python Dictionaries - Quick Guide
📌 1. Basics
Dictionary = Collection of key-value pairs

Key must be unique, Value can be anything

Created with {} or dict()

python

# Create

person = {"name": "John", "age": 25}
empty = {}
📌 2. Access Values
python
person = {"name": "John", "age": 25}

# Method 1: [] - Crashes if key missing

print(person["name"]) # John

# Method 2: get() - Safe, returns None if missing

print(person.get("name")) # John
print(person.get("height")) # None
print(person.get("height", 0)) # 0 (default)
📌 3. Add/Update
python
car = {}
car["brand"] = "Toyota" # Add
car["year"] = 2020 # Add
car["year"] = 2021 # Update

car.update({"color": "red", "price": 25000})
📌 4. Remove Items
python
student = {"name": "John", "age": 21}
age = student.pop("age") # Remove & return value
item = student.popitem() # Remove last item
del student["name"] # Remove key
student.clear() # Empty dictionary
📌 5. Useful Methods
python
person = {"name": "Alice", "age": 30}

keys = person.keys() # All keys
values = person.values() # All values
items = person.items() # All key-value pairs

print("age" in person) # Check if key exists
print(len(person)) # Number of items
📌 6. Looping
python
student = {"name": "Raj", "age": 20}

# Loop through keys

for key in student:
print(key)

# Loop through values

for value in student.values():
print(value)

# Loop through both (MOST USED)

for key, value in student.items():
print(f"{key}: {value}")
📌 7. Common Uses
python

# 1. Phone Book

contacts = {"John": "1234", "Sarah": "5678"}

# 2. Configuration

config = {"host": "localhost", "port": 8080}

# 3. Counting

text = "apple banana apple"
words = text.split()
count = {}
for word in words:
count[word] = count.get(word, 0) + 1

# Result: {"apple": 2, "banana": 1}

📌 8. Dictionary vs List
python

# LIST - Access by position/index

fruits = ["apple", "banana"]
print(fruits[0]) # apple

# DICTIONARY - Access by key

fruits = {"first": "apple", "second": "banana"}
print(fruits["first"]) # apple
📌 9. Error Handling
python
person = {"name": "John"}

# WRONG - Crashes

# print(person["height"]) # KeyError

# RIGHT - Safe ways

print(person.get("height")) # None
print(person.get("height", "Unknown")) # Unknown

if "height" in person:
print(person["height"])
else:
print("Not found")
📌 10. Quick Examples
python

# Shopping cart

cart = {"apple": 2, "banana": 5}
prices = {"apple": 10, "banana": 5}

# Calculate total

total = 0
for item, qty in cart.items():
total += prices[item] \* qty
print(f"Total: ₹{total}")
