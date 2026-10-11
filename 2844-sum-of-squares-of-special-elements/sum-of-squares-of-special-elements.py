class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        sum=0
        for i in range(0,len(nums)):
          
            if n%(i+1)==0:
                sum+=nums[i]*nums[i]
        return sum
        