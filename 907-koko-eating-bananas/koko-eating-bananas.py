import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles) #,1,30
        ans = right #30
        
        while left <right:
            mid = (left + right) // 2 #31//2
            
            # Calculate total hours needed at speed 'mid'
            total_hours = sum(math.ceil(p / mid) for p in piles)
            
            if total_hours <= h:
                right= mid       # Valid speed, try to find a smaller one
               
            else:
                left = mid + 1  # Too slow, need higher speed
                
        return left