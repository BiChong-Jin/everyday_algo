class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        res = 0
        points.sort(key=lambda x: (x[0], -x[1]))

        for i in range(len(points) - 1):
            high = points[i][1]
            low = float("-inf")

            for j in range(i + 1, len(points)):
                curr_y = points[j][1]

                if curr_y > high:
                    continue

                if curr_y > low:
                    res += 1
                    low = curr_y

        return res
