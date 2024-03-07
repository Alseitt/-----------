import os
p=(r"/Users/dulatsultanbek/Documents/uni/pp2/lab6/dir-and-files.md/delete.txt")
if os.path.exists(p):
    os.remove(p)
else:
    print("this file does not exist")
