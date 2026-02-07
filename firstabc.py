n = int(input())
s = list(input())

abc = ["A", "B", "C"]

for i in range(len(s)):
    if s[i] in abc:
        abc.remove(s[i])
    if not abc:
        ans = i + 1
        print(str(ans))
        break
