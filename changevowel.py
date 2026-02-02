import sys

s = list(input())
maps = {
        "a" : "A",
        "e" : "E",
        "i" : "I",
        "o" : "O",
        "u" : "U"
        }

for i in range(len(s)):
    if s[i] in maps:
        s[i] = maps[s[i]]

print("".join(s))
