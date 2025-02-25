import re

def match_pattern(s):
    pattern = r'ab{,3}'
    if re.fullmatch(pattern, s):
        return True

strings = open("txt.txt", encoding = "utf-8")
for s in strings:
    a = match_pattern(s)
    if a == True:
        print(s)
