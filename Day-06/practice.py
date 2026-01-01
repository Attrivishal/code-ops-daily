# practice questions for Day 6
# Q1. write a python program that checks a list od server IPs and print whether each server is ain the local network (starts with  "192.168.x.x)  or in the external server


#list of server IPs
server_ips =[
"192.168.1.10",
    "10.0.0.1", 
    "192.168.2.20",
    "8.8.8.8",
    "192.168.0.100",
    "172.16.0.5"
]

# check each server ip using for loop
print("Checking server IPs...")
print("~" *30)

for ip in server_ips:
    if ip.startswith("192.168"):
        print(f"{ip} ->local server network.")
    else:
        print(f"{ip} -> external server.")

print("Checking complete.")
print("~" *30)

# In this practice exercise, we use a "for" loop to automate the analysis of a log file and identify lines containing the word "error." This demonstrates how loops can be used to process data and extract relevant information efficiently.
log_file =[
    "INFO: Operation successful",
    "ERROR: File not found",
    "DEBUG: Connection established",
    "ERROR: Out of memory",
    "NAME: User logged in",
    ]
for line in log_file:
    if "NAME" in line:
        print(line)
    elif "ERROR" in line:
        print(line)




# You have 10 cloud instances. Check each one.
# If instance ID contains "prod", mark as production.
# If instance ID contains "test", skip it.
# Count how many are production vs development.

instances = [
    "web-prod-01", "db-test-01", "cache-prod-02",
    "api-dev-01", "lb-prod-03", "monitor-prod-02"
]
production = 0
development = 0
for i in instances:
    if "prod" in i:  # Fixed: Check in 'i' not 'instances'
        print(f"{i} -> PRODUCTION")
        production += 1  # Fixed: lowercase 'p'
    elif "test" in i:  # Fixed: Check in 'i' not 'instances'
        print(f"{i} -> TEST (SKIPPED)")
    else:
        print(f"{i} -> DEVELOPMENT")
        development += 1
print("-" * 30)  # Fixed: This makes a line of 30 dashes
print("Results:")
print(f"Production: {production} instances")
print(f"Development: {development} instances")
print(f"Test (skipped): {len(instances) - production - development} instances")