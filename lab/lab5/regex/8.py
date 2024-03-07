import re

text = "MayameIsAlseit"

words = re.findall(r'[A-Z][^A-Z]*', text)
print(words)