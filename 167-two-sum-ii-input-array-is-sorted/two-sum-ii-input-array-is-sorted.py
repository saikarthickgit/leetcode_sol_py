class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        left=0
        right=len(nums)-1
        while left<right:
            temp=nums[left]+nums[right]
            if temp==target:
                return [left+1,right+1]
            elif temp<target:
                left+=1
            else:
                right-=1
    

        