class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        sum = 0

        for i in range(1, n):
            res.append(i)
            sum += i

        last_num = -sum
        res.append(last_num)

        return res
