class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maxi = 0
        
        for char in s:
            if char == '(':
                count += 1
                # Update the maximum depth whenever we go deeper
                maxi = max(maxi, count)
            elif char == ')':
                count -= 1
                
        return maxi
        