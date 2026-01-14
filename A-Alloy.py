import sys

input = sys.stdin.readline()
a, b = input.split()
a, b = int(a), int(b)

if a > 0 and b == 0:
    print("Gold")

elif a == 0 and b > 0:
    print("Silver")

elif a > 0 and b > 0:
    print("Alloy")
