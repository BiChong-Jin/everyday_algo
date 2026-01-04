class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            div_counts = 0
            dummy_div = 1
            curr = 0

            while dummy_div <= math.sqrt(num):
                if not num % dummy_div:
                    other_div = num // dummy_div
                    if other_div != dummy_div:
                        curr += dummy_div
                        curr += other_div
                        div_counts += 2
                    else:
                        curr += dummy_div
                        div_counts += 1

                dummy_div += 1

            if div_counts == 4:
                res += curr

        return res
