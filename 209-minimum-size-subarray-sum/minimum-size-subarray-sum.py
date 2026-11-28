class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        temp = float('inf')

        if target > sum(nums):
            return 0

        sumi = 0
        left = 0

        for i in range(n):
            sumi += nums[i]
            while sumi >= target:
                temp = min(temp, i - left + 1)
                sumi -= nums[left]
                left += 1

        return temp