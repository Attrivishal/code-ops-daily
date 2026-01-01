# without execption handling crashes
a = 20
b = 0
result = a/b
# print(result)

# with execption handling
try:
  a = 20
  b = 0
  result =a /b
except ZeroDivisionError:
  print("cannot divide by zero")