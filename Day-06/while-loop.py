# explain while loop in details in word
count = 0
while count < 5:
    print(f"Count is: {count}")
    if count == 2:
      print("Count reached 2, exiting the loop with the help of break.")
      break # Exit the loop when count is 2
    count += 1  # Increment the count to avoid infinite loop


# continue
print("-" *30)
print("Demonstrating continue statement:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Printing even numbers from the list:")
index = 0
while index < len(numbers):
    if numbers[index] % 2 != 0:
        index += 1
        continue  # Skip odd numbers
    print(numbers[index])
    index += 1

# Newline in middle of text
print("\nSecond line")


# suppose i have a folder with x number of files and i want to process each file one by one until all files are processed and after that  i want to print a message saying all files are processed.
files = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]
index = 0
print("Starting file processing...")
print("-" *30)
while index < len(files):
    print(f"Processing {files[index]}...")# Simulate file processing with a print statement
    print(f"{files[index]} processed.")
    index += 1  # Move to the next file
print("Congrat's All files have been processed.")
print("-" *30)

# Write a program that simulates checking server health status. Keep monitoring until all servers are healthy.
servers = ["Web Server", "Database Server", "Cache Server","load Balancer"]  

status =["Unhealthy","Unhealthy","Unhealthy","Unhealthy"]  # Initial status of servers
print("Fixing  servers... ")
print("~" *30)
server_count=0
while server_count < len(servers):
    status[server_count] = "Healthy"
    print(f"Fixed -> {servers[server_count]}")  # Simulate fixing the server
    server_count+= 1

print("All servers are now healthy!")
print("~" *30)




