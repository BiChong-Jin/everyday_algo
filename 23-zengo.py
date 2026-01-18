import sys

input = sys.stdin.readline
a, b, c = map(int, input().split())

if (a + c) == b:
    if c > 0:
        print(f"{a} -> {b} (+{c})")
    else:
        print(f"{a} -> {b} ({c})")

if (b + c) == a:
    if c > 0:
        print(f"{b} -> {a} (+{c})")

    else:
        print(f"{b} -> {a} ({c})")
