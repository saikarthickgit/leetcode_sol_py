class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        i=n
        right=[0]*n
        left=[0]*n
        result=[0]*n
        if n<=1 or n==0:
            return right

        for i in range(1,n):
            right[i]=right[i-1]+nums[i-1] 
        
        
        for i in range(n-2,-1,-1):
            left[i]=left[i+1]+nums[i+1]
       

        for i in range(n):
            result[i] = abs(left[i] - right[i])
        return result


        