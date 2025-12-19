class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        num = int("".join(str(digit) for digit in digits))

        num += 1
        str_num = str(num)

        ans = []
        for digit in str_num:
            ans.append(digit)

        return [int(e) for e in ans]
