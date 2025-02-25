import re

def match_pattern(s):
    pattern = r'^[a-z]+_[a-z]+$'
    if re.fullmatch(pattern, s):
        return True

strings = open("txt.txt", encoding = "utf-8")
for s in strings:
    if match_pattern(s) == True:
        print(s)
