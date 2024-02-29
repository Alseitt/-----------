import re

text = "MyNameIsA;lseit"

words = re.findall(r'[A-Z][^A-Z]*', text)
print(words)