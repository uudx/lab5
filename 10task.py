import re

strings = open("txt.txt", encoding = "utf-8")

for line in strings:
    if line.isupper():
        print(line.lower())
        continue
    print(re.sub(r'(?<!^)(?=[A-Z А-Я])', '_', line.lower()))
