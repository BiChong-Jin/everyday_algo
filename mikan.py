n = int(input())

if n <= 3:
    print("0")
    exit()

eaten = 0
while n >= 0:
    if eaten < 3:
        eaten += 1
    else:
        res = n
        print(str(res))
        exit()
    n -= 1

ans = n - 3
print(str(ans))
