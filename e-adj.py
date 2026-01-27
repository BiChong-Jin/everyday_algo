import sys

input_stream = sys.stdin.readline

n, q = map(int, input().split())

balls = list(range(1, n + 1))
for _ in range(q):
    x = int(input())

    idx_x = balls.index(x)

    if x == balls[-1]:
        idx_left = idx_x - 1
        x = balls[idx_x]
        left = balls[idx_left]

        balls[idx_x] = left
        balls[idx_left] = x

    else:
        idx_right = idx_x + 1
        x = balls[idx_x]
        right = balls[idx_right]

        balls[idx_x] = right
        balls[idx_right] = x

print(*balls)
