x = int(input())

if x > 0:
    h, m = 11, 60
    m -= x
    ans = f"{h}:{m}"
    print(ans)
    exit()

else:
    h, m = 12, 0
    m += x * (-1)
    if m == 10:
        print("12:00")
        exit()

    else:
        ans = f"{h}:0{m}"
        print(ans)
        exit()
