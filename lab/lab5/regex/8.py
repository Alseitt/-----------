import re

text = "MyNameIsAlseit"

words = re.findall(r'[A-Z][^A-Z]*', text)
print(words)