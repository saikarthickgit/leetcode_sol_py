class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        temp=-1
        maxi=max(nums)
        start=nums[0]
        end=nums[-1]
        if target<start:
            for i in range(n-1,0,-1):
                if nums[i]==target:
                    temp=i
                    break
        else:
            for i in range(0,n):
                if nums[i]==target:
                    temp=i
                    break

        return temp
        
        