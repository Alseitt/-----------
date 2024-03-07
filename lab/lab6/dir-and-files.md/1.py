import os

path = input()
print("Directories:")
for i in os.listdir(path):
    if os.path.isdir(os.path.join(path, i)):
        print(i)
print("\nFiles")
for i in os.listdir(f"{path}"):
    print(i)
print("\nAll Directories and Files:")
for root, directories, files in os.walk(path):
    print(f"\nDirectory: {root}")
    print("Directories:")
    for directory in directories:
        print(os.path.join(root, directory))

