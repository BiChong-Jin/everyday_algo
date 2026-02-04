import sys

ipt_stream = sys.stdin.readline

n = int(input())
taka = []

for i in range(n):
    line = input()
    if line.startswith("Aoki"):
        continue
    name, time_str = line.split()
    time = int(time_str)
    idx = i + 1

    time_to_idx = (time, idx)
    taka.append(time_to_idx)

taka.sort()
print(str(taka[0][1]))
