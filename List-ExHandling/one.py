import os

def create_directories():
    
    print("Directory Creator")
    dirs_input = input("Enter directory names to create (space-separated): ")
    
    if not dirs_input.strip():
        print("No directories specified!")
        return
    
    directories = dirs_input.split()
    
    for dir_name in directories:
        try:
            os.makedirs(dir_name, exist_ok=True)
            print("Created:", dir_name)
        except PermissionError:
            print("No permission to create:", dir_name)
        except Exception as e:
            print("Failed to create", dir_name, ":", e)

create_directories()