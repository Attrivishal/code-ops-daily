# List all the files in list of folders that user provides. 
import os

folders = input("Please  provide list of folder name with spaces in between: ").split()
for folder in folders:
    
    try: 
      files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name: ")
        break


        print("====listing files in -" + folder)
  
        for file in files:
          print(file)





