import re

strings = open("txt.txt", encoding = "utf-8")
print(re.sub(r'(?<!^)(?=[A-Я])', r' ', strings.read()))
