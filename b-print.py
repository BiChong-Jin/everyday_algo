n = int(input())
ans = ""

prev_is_1 = True  # Start with 1
for i in range(n * 2 + 1):  # We need 2n+1 characters for n=10 (21 characters)
    if prev_is_1:
        ans += "1"
        prev_is_1 = False
    else:
        ans += "0"
        prev_is_1 = True

print(ans)
