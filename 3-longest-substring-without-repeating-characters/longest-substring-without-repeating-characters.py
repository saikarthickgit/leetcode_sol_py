class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = []
        maxi = 0
        
        for char in s:
            # Keep popping from the FRONT (queue behavior) until the duplicate is gone
            while char in temp:
                temp.pop(0) 
                
            temp.append(char)
            maxi = max(maxi, len(temp))
            
        return maxi