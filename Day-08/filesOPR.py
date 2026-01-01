# def update_server_config(file_path,key, value ):

#     with open(file_path,"r") as file:
#         lines = file.readlines()

#     with open(file_path,"w") as file:
#         for line in lines:
#             if key in line:
#                 file.write(key + "=" + value + "\n")
#             else:
#                 file.write(line)

# update_server_config("server.conf", "TIMEOUT", "50")
# update_server_config("server.conf", "PORT", "3000")



"Basic file operation"
"A. Read file"
# method 1: READ ALL AT ONCE
# with open("file.txt", "r") as f :
#       content =f.read()
#       print(content)  

# method 2: READ LINE BY LINE 
# with open("file.txt", "r") as f :
#   for line in f:
#     print(line.strip()) # strip() is used for remove the extra line between the text

# method 3: READ ALL LINE AS LIST
# with open("file.txt", "r") as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line.strip())


"B. Write a file"
# overwrite everything
# with open("file.txt","w") as f :
#     f.write("Hey! it me Khushi \n")
#     f.write("How are you doing guys? \n")
#     print("File written Successfully!")

" Append (adds to end) content in file"
# with open("file.txt","a") as f :
#   f.write("What is the plan for today?")
#   print("Data added Successfully!")

"Check if file exists"
# import os

# if os.path.exists("server.confg"):
#       print("File exists!")
# else:
#       print("File doesn't exists!")


" 2. Real-world example"
# 1. ADD USER
def add(name, email, age):
    with open("users.txt", "a") as f:
        f.write(f"{name},{email},{age}\n")
    print(f"+ {name}")

# 2. SHOW ALL  
def show():
    try:
        with open("users.txt", "r") as f:
            for line in f:
                if line.strip():
                    n, e, a = line.strip().split(",")
                    print(f"{n} | {e} | {a}")
    except:
        print("Empty")

# 3. FIND USER
def find(name):
    try:
        with open("users.txt", "r") as f:
            for line in f:
                if line.startswith(name + ","):
                    print(f" {line.strip()}")
                    return
        print(f" {name}")
    except:
        print("Empty")

# USE IT
add("vishal", "vishal@gmail.com", "21")
add("john", "john@gmail.com", "25")
show()
find("vishal")
find("unknown")