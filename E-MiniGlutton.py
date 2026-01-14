import sys

input = sys.stdin.readline

n, x, y = map(int, input().split())
sweet_arr = input().split()
salt_arr = input().split()

sweet_arr.sort(reverse=True)
salt_arr.sort(reverse=True)

sweet_cnts, sweet_sum = 0, 0
salt_cnts, salt_sum = 0, 0

for food in sweet_arr:
    sweet_sum += int(food)
    sweet_cnts += 1
    if sweet_sum > x:
        break

for food in salt_arr:
    salt_sum += int(food)
    salt_cnts += 1
    if salt_sum > y:
        break
ans = min(sweet_cnts, salt_cnts)
print(ans)
