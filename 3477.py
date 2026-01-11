class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        remove_f = 0

        for f in fruits:
            for i in range(len(baskets)):
                if f <= baskets[i]:
                    remove_f += 1
                    baskets[i] = float("-inf")
                    break

        return len(fruits) - remove_f
