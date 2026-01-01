# age checking using execption handling

def check_age():
    try:
        age = int(input("Please Enter your Age: "))
        if age < 0:
            print("Age cannot be negative")
        elif age <18:
            print("You are minor: ")
        else:
            print("You are an adult: ")
    except ValueError:
      print("please enter a valid number:")
      
check_age()
