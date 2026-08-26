class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_len = 0
        zero_count = 0

        for right in range(len(nums)):
            # Expand the window: count zeros
            if nums[right] == 0:
                zero_count += 1

            # Shrink the window from the left if zeros exceed k
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Calculate the current valid window length
            max_len = max(max_len, right - left + 1)

        return max_len