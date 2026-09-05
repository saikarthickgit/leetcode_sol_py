class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # suffix min
        suffix_min = [0] * n
        suffix_min[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suffix_min[i] = min(suffix_min[i+1], nums[i])

        left_max = float('-inf')

        for i in range(n):
            left_max = max(left_max, nums[i])

            if left_max - suffix_min[i] <= k:
                return i

        return -1