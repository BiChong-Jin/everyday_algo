from collections import *

s = list(input())

cnter_s = Counter(s)

for char, cnts in cnter_s.items():
    if cnts >= 2:
        print("No")
        exit()

contain_upper, contain_lower = False, False

for char, cnts in cnter_s.items():
    if char == char.upper():
        contain_upper = True

    if char == char.lower():
        contain_lower = True

if contain_lower and contain_upper:
    print("Yes")
    exit()

print("No")
