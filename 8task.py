import re

strings = open("txt.txt", encoding = "utf-8")
for i in re.split("(?=[A-Z])", strings.read()):
    print(i)
