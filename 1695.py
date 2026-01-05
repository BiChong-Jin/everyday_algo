class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        duplicate = set()
        res = curr_res = left = 0

        for num in nums:
            while num in duplicate:
                curr_res -= nums[left]
                duplicate.remove(nums[left])
                left += 1

            duplicate.add(num)
            curr_res += num
            res = max(res, curr_res)

        return res
