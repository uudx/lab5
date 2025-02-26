import re

strings = open("txt.txt", encoding = "utf-8")
a = re.sub(r"[_]+", r"", strings.read())
print(a)
