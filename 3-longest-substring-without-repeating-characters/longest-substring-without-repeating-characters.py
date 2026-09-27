class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        maxi = 0  
        
        for i, j in enumerate(s):
            if j in seen and seen[j] >= left:
                left = seen[j] + 1
                
            seen[j] = i
            maxi = max(maxi, i - left + 1)
            
        return maxi