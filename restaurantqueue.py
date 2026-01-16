import sys
from collections import deque

input = sys.stdin.readline


def main():
    q = int(input())
    queue = deque()

    for i in range(q):
        line = input()
        if line.startswith("1"):
            _, number = line.split()
            queue.append(number)
        else:
            out = queue.popleft()
            print(out)


if __name__ == "__main__":
    main()
