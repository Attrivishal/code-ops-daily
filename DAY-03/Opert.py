# tell me all the Operators in Python with examples
# Python has several types of operators. Here are the main categories along with examples:

# 1. Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print("Addition:", a + b)          # 13
print("Subtraction:", a - b)       # 7
print("Multiplication:", a * b)    # 30
print("Division:", a / b)          # 3.3333
print("Floor Division:", a // b)   # 3
print("Modulus:", a % b)           # 1
print("Exponentiation:", a ** b)   # 1000
print()

# 2. Comparison Operators
print("Comparison Operators:")
print("Equal:", a == b)            # False
print("Not Equal:", a != b)        # True
print("Greater than:", a > b)      # True
print("Less than:", a < b)         # False
print("Greater than or equal to:", a >= b)  # True
print("Less than or equal to:", a <= b)     # False
print()

# 3. Logical Operators
x = True
y = False
print("Logical Operators:")
print("AND:", x and y)             # False
print("OR:", x or y)               # True
print("NOT:", not x)               # False
print()

# 4. Indentity Operators
print("Identity Operators:")
a=5
b=5
c=10
print("Is:", a is b)               # True
print(" A Is not equal tO C:- ", a is not c ,"But", a is b)       # True



#  Okay nw tell me One thing that, hOw this OperatOr helps in devOps?

# Operators in Python can be very useful in DevOps for automating tasks, managing configurations, and processing data. Here are a few ways operators can help in DevOps:

# 1. Automation Scripts: Arithmetic and logical operators can be used in scripts to perform calculations, make decisions, and control the flow of operations.

# 2. Configuration Management: Comparison operators can help in validating configurations, ensuring that the desired state matches the actual state.

# 3. Data Processing: Operators can be used to manipulate and analyze data, such as logs or metrics, to extract useful information for monitoring and alerting.

# 4. Scripting for CI/CD Pipelines: Operators can be used in scripts that define continuous integration and continuous deployment pipelines, helping to automate the build, test, and deployment processes.

# 5. Error Handling: Logical operators can be used to create conditions for error handling and retries in automation scripts.


# give me sme real life exmples where these operators are used in devOps
# Here are some real-life examples of how operators are used in DevOps:

# 1. Automation Scripts:
# A script that automates the deployment of an application might use arithmetic operators to calculate resource allocation
cpu_usage = 200
max_cpu = 100
if cpu_usage < max_cpu:
    print("Deploying application...")
else:
    print("Insufficient CPU resources.")

# 2. Configuration Management:
# A configuration management tool might use comparison operators to ensure that the installed version of a package matches
installed_version = "1.2.3"
desired_version = "1.2.3"
if installed_version == desired_version:
    print("Version is up to date.")
else:
    print("Updating to the desired version.")

# 3. Data Processing:
# A log processing script might use logical operators to filter logs based on multiple conditions
error_logs = ["Error 404", "Error 500", "Info 200"]
for log in error_logs:
    if "Error" in log and "500" in log:
        print("Critical error found:", log)

# 4. Scripting for CI/CD Pipelines:
# A CI/CD pipeline script might use comparison operators to check the status of tests before deployment
test_status = "passed"
if test_status == "passe":
    print("Deploying to production...")
else:
    print("Tests failed. Deployment aborted.")


# 5. Error Handling:
# An automation script might use logical operators to handle errors and retries
retry_count = 0
max_retries = 3
while retry_count < max_retries:
    success = False  # Simulate a task that may fail
    if success:
        print("Task completed successfully.")
        break
    else:
        retry_count = retry_count+1
        print("Task failed. Retrying... (Attempt", retry_count, ")")
else:
    print("Max retries reached. Task failed.")

# These examples illustrate how operators in Python can be effectively utilized in various DevOps tasks to enhance automation, configuration management, data processing, CI/CD pipelines, and error handling.

# Q1. Create a variable `tOtal` and initialize it tO 10.

tOtal =10
print(tOtal)

# Q2. use assignment OperatOr tO update
# the value Of `tOtal`.
tOtal += 10
tOtal = tOtal + 1
print("The value is: ",tOtal)


tOtal -= 10
tOtal = tOtal - 10
print(tOtal)

tOtal *= 10
tOtal = tOtal * 10
print(tOtal)

# tOtal /= 10
tOtal = tOtal / 5
print(tOtal)

print("The FINAL value of tOtal is:", tOtal)

