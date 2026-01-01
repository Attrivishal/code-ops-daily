# i want to make calculator by taking input from user
num1= int(input("ENTER FIRST NUMBER: "))
num2= int(input("ENTER SECOND NUMBER: ")) 
def addition():
  sum= num1 + num2
  print("ADDITION IS :", sum)

def subtraction():
  sub= num2 - num1
  print("SUBTRACTION IS :", sub)

def multiplication():
  mul= num1 * num2
  print("MULTIPLICATION IS :", mul)

def division():
  div= num2 / num1
  print("DIVISION IS :", div)

addition()
subtraction()
multiplication()
division()