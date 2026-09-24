class Solution:
    def smallestIndex(self, nums):

        def repeat_it(nums):
            temp=0
            while nums>0:
                temp+=nums%10
                nums=nums//10
            return temp
    
        for i in range(len(nums)):
            if i == repeat_it(nums[i]):
                return i
        return -1
    
