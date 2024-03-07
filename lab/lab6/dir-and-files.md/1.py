# DIRECTORY AND File

# 1. Write a Python program to list only directories, files and all directories, files in a specified path.

# import os

# def list_items(path):
#     print("Directories:")
#     for item in os.listdir(path):
#         if os.path.isdir(os.path.join(path, item)):
#             print(item)

#     print("\nFiles:")
#     for item in os.listdir(path):
#         if os.path.isfile(os.path.join(path, item)):
#             print(item)

#     print("\nAll directories and files:")
#     for item in os.listdir(path):
#         print(item)

# # Specify the path
# path = "."  # Current directory

# # List directories, files, and all directories and files in the specified path
# list_items(path)


# 2.Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path

# import os

# def check_path_access(path):
#     # Check if the path exists
#     if not os.path.exists(path):
#         print(f"The path '{path}' does not exist.")
#         return

#     # Check readability
#     if os.access(path, os.R_OK):   #it can be viewed, copied, located 
#         print(f"The path '{path}' is readable.")
#     else:
#         print(f"The path '{path}' is not readable.")

#     # Check writability   #it can be changed
#     if os.access(path, os.W_OK):
#         print(f"The path '{path}' is writable.")
#     else:
#         print(f"The path '{path}' is not writable.")

#     # Check executability   #it can be runed at the terminal
#     if os.access(path, os.X_OK):
#         print(f"The path '{path}' is executable.")
#     else:
#         print(f"The path '{path}' is not executable.")

# # Specify the path to check
# path = "__pycache__"

# # Check access to the specified path
# check_path_access(path)


# 3. Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.

# import os

# path = r"C:\Users\Admin\Desktop\Новая папка\lab\lab6\dir-and-files.md"  #Downloads is a directory that contains files and possibly other directories.

# if os.path.exists(path):
#     print("Path exists")
#     directory, filename = os.path.split(path)
#     print("Directory:", directory)
#     print("Filename:", filename)
# else:
#     print("Path does not exist")


# 4. Write a Python program to count the number of lines in a text file.

# filename = 'drafttext.txt'
# with open(filename, 'r') as file:
#     num_lines = 0
#     for line in file:
#         num_lines += 1

# print(f'The number of lines in {filename} is: {num_lines}')


# 5. Write a Python program to write a list to a file.

# my_list = ["apple", "banana", "cherry", "date"]

# # Open a file in write mode
# with open("my_list.txt", "w") as file:  #with statement automatically closes the file after the for loop completes, ensuring that all data is written to the file 
#     # Loop through the list and write each string to a new line in the file
#     for item in my_list:
#         file.write(item + "\n")  #"\n" ensures that each item is written to a new line in the file.


# 6. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

# import string

# # Loop through each uppercase letter
# for letter in string.ascii_uppercase:  #string.ascii_uppercase constant to generate them automatically
#     # Create the filename
#     filename = letter + ".txt"
#     # Open the file and write the message
#     with open(filename, "w") as file:
#         file.write("This is file " + filename)


# 7. Write a Python program to copy the contents of a file to another file

# Source file path
# source_file = "source.txt"

# # Destination file path
# destination_file = "destination.txt"

# # Open the source file in read mode and the destination file in write mode
# with open(source_file, "r") as source, open(destination_file, "w") as destination:
#     # Read the contents of the source file
#     contents = source.read()
#     # Write the contents to the destination file
#     destination.write(contents)

# print("File copied successfully.")


# 8. Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.


# import os

# file_path = r"C:\Users\alser\Downloads\githowto\githowto\repositories\work\delete.txt"

# if os.path.exists(file_path):
#     # Check if the user has permission to delete the file
#     if os.access(file_path, os.W_OK):
#         # Delete the file
#         os.remove(file_path)
#         print(f"{file_path} has been deleted.")
#     else:
#         print(f"ERROR: You do not have permission to delete {file_path}.")
# else:
#     print(f"ERROR: {file_path} does not exist.")