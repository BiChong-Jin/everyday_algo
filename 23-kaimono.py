import sys

input = sys.stdin.readline

a, b, c, d = map(int, input().split())

if c >= a or d >= b:
    print("No")
    exit()

print("Yes")
