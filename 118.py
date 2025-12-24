class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for i in range(numRows):
            row = [0 for _ in range(i + 1)]
            row[0], row[-1] = 1, 1

            for space in range(1, len(row) - 1):
                row[space] = res[i - 1][space - 1] + res[i - 1][space]
            res.append(row)

        return res
