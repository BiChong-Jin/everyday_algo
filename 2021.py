import collections
import sys


class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        d = collections.defaultdict(int)
        for i, dis in lights:
            d[i - dis] += 1
            d[i + dis + 1] -= 1
        cur, max_idx, max_val = 0, -1, -sys.maxsize
        for idx, val in sorted(d.items()):
            cur += val
            if cur > max_val:
                max_val, max_idx = cur, idx
        return max_idx
