class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        nums = sorted(set(nums))
        n=len(nums)
        count=0
        maxi=0
        for i in range(1,n):
            if nums[i]-1==nums[i-1]:
                count+=1
                maxi=max(maxi,count)
            else:
                
                count=0
        return maxi + 1 if nums else 0

        