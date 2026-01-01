def calculator():
  print("Simple calculator")
  print("Enter two numbers: ")

  try:
    # first number
    num1 = float(input("First number: "))

    # second number
    num2 = float(input("Enter second number: "))

    # get operation
    operation = input("Operation (+ , -,*,/):")
    # perform calculation
    if operation == '+':
      result = num1 + num2
    elif operation == '-':
      result = num1 - num2
    elif operation == '*':
      result = num1 * num2
    elif operation == '/':
      result = num1 / num2
    else:
      print("Invalid operations: ")
      return

    print(f"Results: {result}")

  except ValueError:
      print("Please enter valid number!")
  except ZeroDivisionError:
      print("Cannot divide by zero")
  except Exception as e:
      print(f"something went wrong: {e}")


calculator()