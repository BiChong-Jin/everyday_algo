import sys

input = sys.stdin.readline

cnts = int(input())
nums = input().split()

dup = set()

for num in nums:
    dup.add(num)

length = len(dup)

if length > 1:
    print("No")
else:
    print("Yes")
