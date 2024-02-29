import re

text = "Hello My name, is. Alseit"
replacedText = re.sub(r'[ ,.]', ':', text)
print(replacedText)