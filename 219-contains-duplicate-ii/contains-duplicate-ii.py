class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {} # Stores the last seen index of each number
        
        for i, num in enumerate(nums):
            # If the number is in the dictionary and the index difference is <= k
            if num in seen and i - seen[num] <= k:
                return True
            
            # Update the last seen index for the current number
            seen[num] = i
            
        return False