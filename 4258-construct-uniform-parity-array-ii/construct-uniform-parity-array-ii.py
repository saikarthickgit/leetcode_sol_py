class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # If all elements are even, we don't need to change anything
        if all(x % 2 == 0 for x in nums1):
            return True
        
        # If there are odd elements, the minimum element must be odd
        return min(nums1) % 2 != 0