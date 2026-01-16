import sys

input = sys.stdin.readline

a, b = input().split()
people = [1, 2, 3]
if a == b:
    print("-1")

else:
    a, b = int(a), int(b)
    low = min(a, b)
    high = max(a, b)
    people.remove(low)
    people.remove(high)

    print(*people)
