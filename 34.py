class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        begin = self.findLowerBound(nums, target, True)
        if begin == -1:
            return [-1, -1]

        end = self.findLowerBound(nums, target, False)
        return [begin, end]

    def findLowerBound(self, nums: List[int], target: int, isFirst: bool) -> int:
        n = len(nums)
        begin, end = 0, n - 1

        while begin <= end:
            mid = (begin + end) // 2

            if nums[mid] == target:
                if isFirst:
                    if mid == begin or nums[mid - 1] != target:
                        return mid

                    end = mid - 1

                else:
                    if mid == end or nums[mid + 1] != target:
                        return mid

                    begin = mid + 1

            elif nums[mid] > target:
                end = mid - 1

            else:
                begin = mid + 1
        return -1
