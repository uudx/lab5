import re

strings = open("txt.txt", encoding = "utf-8")
a = re.sub(r"[ ,.]+", ":", strings.read())
print(a)
