class Solution:
    def findMin(self, nums: List[int]) -> int:
        max_val = max(nums)
        max_idx = nums.index(max_val)

        # If max is at the end, array is not rotated -> min is at index 0
        if max_idx == len(nums) - 1:
            return nums[0]
        # Otherwise, min is directly to the right of max
        return nums[max_idx + 1]