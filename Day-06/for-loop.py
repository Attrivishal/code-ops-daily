# Explain loops in details 
for i in range(4):
  print(f"{i}.vishal Attri")
# In the above code, we are using a 'for' loop to iterate over a range of numbers from 0 to 14.

students_name = ["Vishal", "Ankit", "Khushi", "Riya"]  
for name in students_name:
  print(f"student name: {name}")

# tell me some example related to devops
servers = ["192.168.1.10", "192.168.1.10"]

for server in servers:
    # Check if server is in local network (starts with 192.168)
    if server.startswith("192.168"):
        print(f"Connecting to server: {server}")
    else:
        print(f"Invalid server: {server} - Please connect to a valid server")
    
    # Check the server status
    print(f"Checking connection to {server}...")
    # In real DevOps work, you would ping or SSH here
    print(f"✓ {server} is online")
    print()  # Empty line for readability


