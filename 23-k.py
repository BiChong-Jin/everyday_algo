import sys
from collections import Counter

input = sys.stdin.readline

n, q = map(int, input().split())
s = list(input())

for _ in range(q):
    type, start, end = input().split()
    type = int(type)
    if type == 1:
        start, char = int(start) - 1, end
        s[start] = char

    elif type == 2:
        start, end = int(start) - 1, int(end) - 1
        counts = Counter(s[start : end + 1])
        sorted_cnt = sorted(counts.items(), key=lambda item: item[1], reverse=True)
        print(sorted_cnt[0][1])
