import re

f = open("row.txt", "r", encoding="utf-8")

for line in f:
    if re.fullmatch("^ab*$", line):
        print(line)
