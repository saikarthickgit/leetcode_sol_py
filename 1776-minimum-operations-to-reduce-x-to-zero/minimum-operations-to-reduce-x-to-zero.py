class Solution:
    def minOperations(self, nums, x):
        n = len(nums) #5
        total = sum(nums) #11
        target = total - x #6

        if target < 0:  #base case
            return -1

        if target == 0: #base case
            return n

        left = 0
        s = 0
        longest = -1

        for right in range(n): 

            s += nums[right] 

            while left <= right and s > target:
                s -= nums[left]
                left += 1

            if s == target:
                longest = max(longest, right - left + 1)

        return -1 if longest == -1 else n - longest