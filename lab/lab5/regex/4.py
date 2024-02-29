import re

pattern = re.compile(r"[A-Z]{1}[a-z]+")
print(pattern.findall("Alseit Zhauken programming Principles 2"))
