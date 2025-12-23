class SparseVector:
    def __init__(self, nums: List[int]):
        self.pairs = []

        for idx, val in enumerate(nums):
            if val != 0:
                self.pairs.append([idx, val])

    def dotProduct(self, vec: "SparseVector") -> int:
        res = 0
        p, q = 0, 0

        while p < len(self.pairs) and q < len(vec.pairs):
            if self.pairs[p][0] == vec.pairs[q][0]:
                res += self.pairs[p][1] * vec.pairs[q][1]
                p += 1
                q += 1

            elif self.pairs[p][0] < vec.pairs[q][0]:
                p += 1

            else:
                q += 1

        return res
