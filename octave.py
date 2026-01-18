import sys

input = sys.stdin.readline

n = int(input())
res = [int(e) for e in input().split()]

first, idx1 = min(res), res.index(min(res))
res[idx1] = float("inf")

second, idx2 = min(res), res.index(min(res))
res[idx2] = float("inf")

third, idx3 = min(res), res.index(min(res))

print(idx1 + 1, idx2 + 1, idx3 + 1)
