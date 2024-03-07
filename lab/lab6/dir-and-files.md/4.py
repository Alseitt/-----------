import os

f = open(r"/Users/dulatsultanbek/Documents/uni/pp2/lab6/dir-and-files.md/4.txt")
cnt = 0
for lines in f:
    cnt += 1
print(f"file has {cnt} lines")
