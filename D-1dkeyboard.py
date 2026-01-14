import sys

input = sys.stdin.readline

arr_s = list(input())
arr_pair = []

for idx, char in enumerate(arr_s):
    arr_pair.append([char, idx])

arr_pair.sort()

ans = 0

for i in range(1, len(arr_pair)):
    if arr_pair[i][0] == "A":
        continue
    ans += abs(arr_pair[i][1] - arr_pair[i - 1][1])

print(ans)
