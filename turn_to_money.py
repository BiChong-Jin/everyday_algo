import sys

ipt_stream = sys.stdin.readline 

n = int(input())
a = list(int(e) for e in input().split())
p = list(int(e) for e in input().split())

ans = 0
for x, y in zip(a, p):
    t = p[x - 1]
    ans += t

print(str(ans))
