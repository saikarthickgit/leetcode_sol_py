class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n=len(nums)
        first, sec=0,0
        nums.sort(key=abs,reverse=True)
        i=0
        t=(n+1)//2
        while i<n:
            if i<t:
                first+=nums[i]*nums[i]
                
            else:
                sec+=nums[i]*nums[i]
            i+=1
        return first-sec