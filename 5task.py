import re

def match_pattern(s):
    pattern = r'^a.+b$'
    if re.fullmatch(pattern, s):
        return True

strings = open("txt.txt", encoding = "utf-8")
for s in strings:
    if match_pattern(s) == True:
        print(s)
