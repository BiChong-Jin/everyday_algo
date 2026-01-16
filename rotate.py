import sys

input = sys.stdin.readline

abc = input().strip()
abc_arr = list(abc)

bca_arr = abc_arr[1] + abc_arr[2] + abc_arr[0]
cab_arr = abc_arr[2] + abc_arr[0] + abc_arr[1]

res = int("".join(abc_arr)) + int("".join(bca_arr)) + int("".join(cab_arr))

print(res)
